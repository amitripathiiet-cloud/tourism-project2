from huggingface_hub import HfApi
import os
# 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
api = HfApi(token=os.getenv("HF_TOKEN"))
api.upload_folder(
    folder_path="/content/tourism_project/deployment",     # the local folder containing your files
    repo_id="Amittripipathi/tourism-project",          # the target repo
    repo_type="space",                      # dataset, model, or space
    path_in_repo="",                          # optional: subfolder path inside the repo
)
