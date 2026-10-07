# MarketBoard 公开网页部署

此仓库只保存工作流与保留策略。网页、JSON 和历史快照由工作流生成。采集源码保存在私有仓库。

仓库 Settings → Secrets and variables → Actions 中设置：

- `PRIVATE_REPO_READ_TOKEN`：仅有私有采集仓库 Contents: Read 权限的 fine-grained token。
- `DATABULL_API_KEY`：可选；DataBull 免费密钥。未设置仍使用无密钥来源。
- 仓库变量 `PRIVATE_SOURCE_REPO`：形如 `owner/marketboard-source-private`。

Settings → Pages → Build and deployment → Source 选 **GitHub Actions**。工作流可手动执行，也会每日北京时间约 19:30、次日 07:30 自动运行。GitHub 定时任务可能延迟；看板始终显示各条数据真实交易日期。

每次发布成功后，工作流会更新一次 `last-successful-run.txt`。这是为了使公开仓库保持活动状态，避免 GitHub 将长期无提交的公开仓库定时工作流自动停用。

前端的“读取最新数据”只重新读取已发布 JSON。用户不能从公开网页触发采集或修改资产。北京时间早间定时运行会生成一个 `snapshot-YYYY-MM-DD` Release；超过 90 天自动清理。
