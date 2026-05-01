import os

from github import Github


class GitHubIntegration:
    def __init__(self, token=None):
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.client = Github(self.token) if self.token else None

    def get_repo_info(self, repo_name):
        if not self.client:
            return {"error": "GitHub authentication required. Set GITHUB_TOKEN."}
        try:
            repo = self.client.get_repo(repo_name)
            return {
                "status": "success",
                "name": repo.full_name,
                "stars": repo.stargazers_count,
                "open_issues": repo.open_issues_count,
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def trigger_action(self, repo_name, workflow_id):
        if not self.client:
            return {"error": "GitHub authentication required. Set GITHUB_TOKEN."}
        try:
            repo = self.client.get_repo(repo_name)
            workflow = repo.get_workflow(workflow_id)
            workflow.create_dispatch(ref="main")
            return {"status": "success", "message": f"Triggered workflow {workflow_id}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
