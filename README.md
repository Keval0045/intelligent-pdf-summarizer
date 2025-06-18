# Intelligent PDF Summarizer

This project uses Azure Durable Functions to ingest PDFs, extract their text using Form Recognizer, summarize the text using Azure OpenAI, and save the summary to blob storage.

## 🔧 Setup Instructions

1. Install Python 3.9+ and Azure Functions Core Tools.
2. Start Azurite.
3. Create `input` and `output` blob containers.
4. Create a `local.settings.json` file (see sample below).
5. Install dependencies:
   ```bash
   python3 -m pip install -r requirements.txt
   ```
6. Start the app:
   ```bash
   func start --verbose
   ```

## 📁 local.settings.json sample
```json
{
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "AzureWebJobsFeatureFlags": "EnableWorkerIndexing",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "BLOB_STORAGE_ENDPOINT": "<BLOB-STORAGE-ENDPOINT>",
    "COGNITIVE_SERVICES_ENDPOINT": "<COGNITIVE-SERVICE-ENDPOINT>",
    "AZURE_OPENAI_ENDPOINT": "<AZURE-OPEN-AI-ENDPOINT>",
    "AZURE_OPENAI_KEY": "<AZURE-OPEN-AI-KEY>",
    "CHAT_MODEL_DEPLOYMENT_NAME": "<AZURE-OPEN-AI-MODEL>"
  }
}
```