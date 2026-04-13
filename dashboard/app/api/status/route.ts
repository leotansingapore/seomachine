import { NextResponse } from "next/server";

const GH_USER = "leotansingapore";
const REPOS = [
  { name: "seomachine", role: "Content Engine", emoji: "M" },
  { name: "seo-audit-tool", role: "Audit Dashboard", emoji: "A" },
  { name: "build-the-best", role: "Client Platform", emoji: "P" },
];

async function fetchGitHub(path: string) {
  const token = process.env.GITHUB_TOKEN;
  const headers: Record<string, string> = {
    Accept: "application/vnd.github+json",
  };
  if (token) headers.Authorization = `Bearer ${token}`;
  const res = await fetch(`https://api.github.com/${path}`, {
    headers,
    next: { revalidate: 300 },
  });
  if (!res.ok) return null;
  return res.json();
}

export async function GET() {
  const since = new Date(Date.now() - 7 * 24 * 60 * 60 * 1000).toISOString();

  const repoData = await Promise.all(
    REPOS.map(async (repo) => {
      const [commits, issues, pulls] = await Promise.all([
        fetchGitHub(
          `repos/${GH_USER}/${repo.name}/commits?since=${since}&per_page=30`
        ),
        fetchGitHub(
          `repos/${GH_USER}/${repo.name}/issues?state=open&per_page=100`
        ),
        fetchGitHub(
          `repos/${GH_USER}/${repo.name}/pulls?state=open&per_page=10`
        ),
      ]);

      const recentCommits = (commits || []).map(
        (c: {
          sha: string;
          commit: {
            message: string;
            author: { date: string };
          };
        }) => ({
          sha: c.sha.slice(0, 7),
          message: c.commit.message.split("\n")[0],
          date: c.commit.author.date,
        })
      );

      return {
        ...repo,
        commits: recentCommits,
        commitCount: recentCommits.length,
        issueCount: (issues || []).filter(
          (i: { pull_request?: unknown }) => !i.pull_request
        ).length,
        prCount: (pulls || []).length,
        lastCommit: recentCommits[0]?.date || null,
      };
    })
  );

  const totalCommits = repoData.reduce((s, r) => s + r.commitCount, 0);

  return NextResponse.json({
    repos: repoData,
    totalCommits,
    generatedAt: new Date().toISOString(),
    window: "7 days",
  });
}
