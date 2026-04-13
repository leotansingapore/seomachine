"use client";

import { useEffect, useState } from "react";

interface Commit {
  sha: string;
  message: string;
  date: string;
}

interface Repo {
  name: string;
  role: string;
  commits: Commit[];
  commitCount: number;
  issueCount: number;
  prCount: number;
  lastCommit: string | null;
}

interface StatusData {
  repos: Repo[];
  totalCommits: number;
  generatedAt: string;
}

const EXTERNAL_LINKS: Record<string, string> = {
  auditDashboard:
    "https://seo-audit-tool-leotansingapores-projects.vercel.app",
  autoSEO: "https://getautoseo.com",
  sheet:
    "https://docs.google.com/spreadsheets/d/17XNZrWmJqWY8fLq5NHSwpl_IiMIZwsBsZdz2uWfUYKw",
  scheduledAgents: "https://claude.ai/code/scheduled",
  seomachine: "https://github.com/leotansingapore/seomachine",
  "seo-audit-tool": "https://github.com/leotansingapore/seo-audit-tool",
  "build-the-best": "https://github.com/leotansingapore/build-the-best",
  "seo-hub-central": "https://github.com/leotansingapore/seo-hub-central",
};

function timeAgo(dateStr: string): string {
  const diff = Date.now() - new Date(dateStr).getTime();
  const hours = Math.floor(diff / 3600000);
  if (hours < 1) return "just now";
  if (hours < 24) return `${hours}h ago`;
  const days = Math.floor(hours / 24);
  if (days === 1) return "yesterday";
  return `${days}d ago`;
}

export default function Home() {
  const [data, setData] = useState<StatusData | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/api/status")
      .then((r) => r.json())
      .then((d) => {
        setData(d);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  return (
    <div className="min-h-screen bg-[#0a0a0a]">
      <header className="border-b border-zinc-800 px-6 py-4">
        <div className="max-w-5xl mx-auto flex items-center justify-between">
          <div>
            <h1 className="text-xl font-semibold tracking-tight">
              SEO Content Machine
            </h1>
            <p className="text-sm text-zinc-500 mt-0.5">
              Autonomous SEO agency ops
            </p>
          </div>
          <div className="flex items-center gap-3 text-xs text-zinc-500">
            <span className="flex items-center gap-1.5">
              <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
              Live
            </span>
            {data && (
              <span>
                Updated{" "}
                {new Date(data.generatedAt).toLocaleTimeString("en-SG", {
                  hour: "2-digit",
                  minute: "2-digit",
                })}{" "}
                SGT
              </span>
            )}
          </div>
        </div>
      </header>

      <main className="max-w-5xl mx-auto px-6 py-8 space-y-8">
        {loading ? (
          <div className="text-center py-20 text-zinc-500">Loading...</div>
        ) : data ? (
          <>
            {/* Stats */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
              <StatCard
                label="Commits (7d)"
                value={data.totalCommits.toString()}
              />
              <StatCard label="Repos" value="4" />
              <StatCard
                label="Open Issues"
                value={data.repos
                  .reduce((s, r) => s + r.issueCount, 0)
                  .toString()}
              />
              <StatCard
                label="Open PRs"
                value={data.repos
                  .reduce((s, r) => s + r.prCount, 0)
                  .toString()}
              />
            </div>

            {/* Repos */}
            <section className="space-y-4">
              <h2 className="text-sm font-medium text-zinc-400 uppercase tracking-wider">
                Repositories
              </h2>
              <div className="grid gap-4">
                {data.repos.map((repo) => (
                  <RepoCard key={repo.name} repo={repo} />
                ))}
              </div>
            </section>

            {/* Architecture */}
            <section className="space-y-4">
              <h2 className="text-sm font-medium text-zinc-400 uppercase tracking-wider">
                System Architecture
              </h2>
              <div className="bg-zinc-900 border border-zinc-800 rounded-lg p-6 font-mono text-xs md:text-sm text-zinc-400 whitespace-pre leading-relaxed overflow-x-auto">
                {`            seomachine (Content Engine)
           /        |        \\         \\
  /discover   /new-client  /publish   /client-report
  /analyze     /write      /autoseo
      v           |            v              v
seo-audit-tool  Pipeline  build-the-best  seo-hub-central
(Audit + KW)   topics->   (AutoSEO)      (Agency CRM)
Google Sheets  draft->     receive-       leads, tasks,
Supabase       published   article        approvals, GSC`}
              </div>
            </section>

            {/* Quick links */}
            <section className="space-y-4">
              <h2 className="text-sm font-medium text-zinc-400 uppercase tracking-wider">
                Quick Links
              </h2>
              <div className="grid grid-cols-2 md:grid-cols-3 gap-3">
                <QuickLink
                  label="Audit Dashboard"
                  href={EXTERNAL_LINKS.auditDashboard}
                  desc="seo-audit-tool"
                />
                <QuickLink
                  label="AutoSEO Platform"
                  href={EXTERNAL_LINKS.autoSEO}
                  desc="build-the-best"
                />
                <QuickLink
                  label="Status Sheet"
                  href={EXTERNAL_LINKS.sheet}
                  desc="Google Sheets"
                />
                <QuickLink
                  label="Scheduled Agents"
                  href={EXTERNAL_LINKS.scheduledAgents}
                  desc="Claude Code"
                />
                <QuickLink
                  label="seomachine"
                  href={EXTERNAL_LINKS.seomachine}
                  desc="GitHub"
                />
                <QuickLink
                  label="seo-audit-tool"
                  href={EXTERNAL_LINKS["seo-audit-tool"]}
                  desc="GitHub"
                />
                <QuickLink
                  label="Agency CRM"
                  href={EXTERNAL_LINKS["seo-hub-central"]}
                  desc="seo-hub-central"
                />
              </div>
            </section>
          </>
        ) : (
          <div className="text-center py-20 text-zinc-500">
            Failed to load status
          </div>
        )}
      </main>

      <footer className="border-t border-zinc-800 px-6 py-4 mt-8">
        <div className="max-w-5xl mx-auto text-xs text-zinc-600 flex justify-between">
          <span>Leo Tan SEO Agency</span>
          <span>Reports: Mon + Thu 9am SGT</span>
        </div>
      </footer>
    </div>
  );
}

function StatCard({ label, value }: { label: string; value: string }) {
  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-lg p-4">
      <div className="text-2xl font-semibold font-mono">{value}</div>
      <div className="text-xs text-zinc-500 mt-1">{label}</div>
    </div>
  );
}

function RepoCard({ repo }: { repo: Repo }) {
  const ghUrl = `https://github.com/leotansingapore/${repo.name}`;
  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-lg p-5">
      <div className="flex items-start justify-between">
        <div>
          <div className="flex items-center gap-2">
            <a
              href={ghUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="text-base font-semibold hover:text-blue-400 transition-colors"
            >
              {repo.name}
            </a>
            <span className="text-xs text-zinc-500 bg-zinc-800 px-2 py-0.5 rounded">
              {repo.role}
            </span>
          </div>
          <div className="flex items-center gap-2 mt-2">
            <StatusBadge count={repo.commitCount} label="commits" />
            <StatusBadge count={repo.issueCount} label="issues" />
            <StatusBadge count={repo.prCount} label="PRs" />
          </div>
        </div>
        <div className="text-xs text-zinc-500 text-right">
          {repo.lastCommit ? (
            <>
              <div>Last commit</div>
              <div className="font-mono">{timeAgo(repo.lastCommit)}</div>
            </>
          ) : (
            <div>No recent activity</div>
          )}
        </div>
      </div>

      {repo.commits.length > 0 && (
        <div className="mt-4 space-y-1.5">
          {repo.commits.slice(0, 5).map((c) => (
            <div
              key={c.sha}
              className="flex items-center gap-2 text-xs text-zinc-400"
            >
              <span className="font-mono text-zinc-600 shrink-0">
                {c.sha}
              </span>
              <span className="truncate">{c.message}</span>
              <span className="text-zinc-600 shrink-0 ml-auto">
                {timeAgo(c.date)}
              </span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

function StatusBadge({ count, label }: { count: number; label: string }) {
  const bg =
    count > 0
      ? label === "issues"
        ? "bg-amber-500/15 text-amber-400"
        : "bg-blue-500/15 text-blue-400"
      : "bg-zinc-800 text-zinc-500";
  return (
    <span className={`px-2 py-0.5 rounded text-xs font-mono ${bg}`}>
      {count} {label}
    </span>
  );
}

function QuickLink({
  label,
  href,
  desc,
}: {
  label: string;
  href: string;
  desc: string;
}) {
  return (
    <a
      href={href}
      target="_blank"
      rel="noopener noreferrer"
      className="bg-zinc-900 border border-zinc-800 rounded-lg p-3 hover:border-zinc-600 transition-colors block"
    >
      <div className="text-sm font-medium">{label}</div>
      <div className="text-xs text-zinc-500 mt-0.5">{desc}</div>
    </a>
  );
}
