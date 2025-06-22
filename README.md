# Intelligent PDF Summarizer using Azure Durable Functions

This project demonstrates how to build a cloud-based Intelligent Document Processing System using Azure Durable Functions, Blob Storage, Cognitive Services, and Azure OpenAI. It enables the automatic extraction and summarization of text from uploaded PDF files.

## Features

- Upload a PDF to Azure Blob Storage
- Automatically trigger Azure Functions when a file is uploaded
- Extract content using Cognitive Services (OCR or Form Recognizer)
- Generate a summary using Azure OpenAI (GPT-based)
- Durable orchestration with retry and monitoring

## Tech Stack

- Azure Functions (Python) with Durable Functions
- Azure Blob Storage – file ingestion trigger
- Azure Cognitive Services – OCR / Document Intelligence
- Azure OpenAI – text summarization using GPT models
- Azure Monitor (optional) – for diagnostics and logs

## Project Structure

IntelligentPdfSummarizer/
|
├── __init__.py                  # Function entry point
├── orchestrator_function.py    # Durable orchestrator
├── activity_extract_text.py    # Extract text from PDF
├── activity_summarize_text.py  # Call Azure OpenAI
├── requirements.txt            # Dependencies
├── local.settings.json         # Local config (gitignored)
├── local.settings.template.json # Template config (safe to share)
└── host.json                   # Azure Functions config

## Setup Instructions

### 1. Clone the Repo
    git clone https://github.com/your-username/IntelligentPdfSummarizer.git
    cd IntelligentPdfSummarizer

### 2. Create a Python Virtual Environment
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate

### 3. Install Dependencies
    pip install -r requirements.txt

### 4. Configure Environment Settings

Never commit your secrets.

- Copy the template file and fill in your actual keys:
    cp local.settings.template.json local.settings.json

- Update local.settings.json with:
    - Your Azure Blob Storage connection string
    - Cognitive Services endpoint
    - OpenAI endpoint and key
    - Your GPT deployment name

### 5. Run Locally

Make sure Azure Functions Core Tools are installed:

    func start

## Deployment to Azure

### Using Azure CLI:

    az functionapp create --resource-group <your-rg> --consumption-plan-location <region> \
      --runtime python --functions-version 4 --name <your-func-app-name> \
      --storage-account <your-storage-account-name>

    func azure functionapp publish <your-func-app-name>

## local.settings.template.json (Safe Example)

{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "<YOUR-STORAGE-STRING-HERE>",
    "AzureWebJobsFeatureFlags": "EnableWorkerIndexing",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "BLOB_STORAGE_ENDPOINT": "<YOUR-BLOB-ENDPOINT>",
    "COGNITIVE_SERVICES_ENDPOINT": "<YOUR-COGNITIVE-ENDPOINT>",
    "AZURE_OPENAI_ENDPOINT": "<YOUR-AZURE-OPENAI-ENDPOINT>",
    "AZURE_OPENAI_KEY": "<YOUR-AZURE-OPENAI-KEY>",
    "CHAT_MODEL_DEPLOYMENT_NAME": "<YOUR-DEPLOYMENT-NAME>"
  }
}

## Best Practices

- Keep local.settings.json out of source control (already in .gitignore)
- Use Key Vault for secret management in production
- Use Application Settings in Azure for environment variables


