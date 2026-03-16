from langchain_core.prompts import PromptTemplate
from utils.llm_factory import get_llm

def generate_insights(analysis: dict, user_question: str = "") -> str:
    llm = get_llm("gemini")

    prompt = PromptTemplate.from_template("""
You are a senior business analyst. Given this dataset analysis:

Summary stats: {summary}
Correlations: {correlations}
Row count: {row_count}, Columns: {column_count}

User question: {question}

Provide:
1. Top 3 business insights
2. Key trends or anomalies
3. Recommendations based on data
Keep it clear and non-technical.
""")

    chain = prompt | llm
    result = chain.invoke({
        **analysis,
        "summary": str(analysis["summary"])[:1500],
        "correlations": str(analysis["correlations"])[:500],
        "question": user_question or "What are the key takeaways?"
    })
    return result.content