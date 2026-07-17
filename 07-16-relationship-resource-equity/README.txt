# 07-16-relationship-resource-equity — 文件夹地图
# 更新：2026-07-16

## 你现在只需要看 02-current/（当前定稿，只有 2 轨）

| 文件 | 是什么 | 谁写的 |
|---|---|---|
| cn-v2-生在温差里.txt | 中文定稿 v2 | Cursor SOL（gpt-5.6-sol-xhigh）按 audit 手术 |
| en-v2-between-temperatures.txt | 英文定稿 v2 | Hermes sub-agent 按 audit 手术 |
| dual-v2-parallel-cn+en+audit.txt | 中英并排 + 完整 audit | 合集，方便一次看完 |

**结论：当前不是 3 版在打架，是「中文 1 轨 + 英文 1 轨」。**

---

## 历史里曾经出现过谁的稿？（避免懵）

| 阶段 | 文件（现已进 archive） | 作者 |
|---|---|---|
| 最早英文试写 | lyric-v1-temporary.txt | Lyric（我 / 主会话） |
| 双线 v1 中文 | cursor-sol-v1-生在温差里.txt | Cursor SOL |
| 双线 v1 英文 | hermes-v1-between-temperatures.txt | Hermes sub-agent |
| audit 后中文 v2 | → 02-current/cn-v2-… | Cursor SOL（定稿） |
| audit 后英文 v2 | → 02-current/en-v2-… | Hermes（定稿） |
| 我本地手术保底 | lyric-surgical-cn/en-v2.txt | Lyric 手改备份（与定稿同向，可忽略） |

所以「3 个作者」都写过，但 **每语言定稿只认 v2 一份**。  
surgical 不是第三定稿，是防 agent 翻车时的备份。

---

## 目录结构

```
00-read-me/          ← 本说明
01-source/           ← 原料：你的 raw、AI 分析、Sonnet、audit、craft
02-current/          ← 只看这里：中英 v2 + 平行合集
03-archive/
  v1/                ← 全部 v1
  v2-backups/        ← surgical 保底
  prompts-logs/      ← 委托 prompt、stdout/stderr
```

---

## 推荐下一步

按 audit：停改词 → 用 02-current/cn-v2 进 Suno（主轨中文）。  
英文轨保留作对照 / 国际版，不强制再磨。
