import azure.functions as func
import azure.durable_functions as df

def orchestrator_function(context: df.DurableOrchestrationContext):
    input_blob = context.get_input()
    pdf_content = yield context.call_activity("download_pdf", input_blob)
    extracted_text = yield context.call_activity("extract_text", pdf_content)
    summary = yield context.call_activity("summarize_text", extracted_text)
    yield context.call_activity("upload_summary", summary)

main = df.Orchestrator.create(orchestrator_function)