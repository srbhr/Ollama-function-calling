import asyncio
from ollama import AsyncClient
from search_tool import web_search, extract_content

async def process_query(query: str) -> str:
    client = AsyncClient()
    
    # Define our search tool
    search_tool = {
        'type': 'function',
        'function': {
            'name': 'web_search',
            'description': 'Search the web for current information on a topic',
            'parameters': {
                'type': 'object',
                'required': ['query'],
                'properties': {
                    'query': {
                        'type': 'string',
                        'description': 'The search query to look up'
                    }
                }
            }
        }
    }

    # First, let Ollama decide if it needs to search
    response = await client.chat(
        'llama3.2',
        messages=[{
            'role': 'user',
            'content': f'Answer this question: {query}'
        }],
        tools=[search_tool]
    )

    # Initialize available functions
    available_functions = {
        'web_search': web_search
    }

    # Check if Ollama wants to use the search tool
    if response.message.tool_calls:
        print("Searching the web...")
        
        for tool in response.message.tool_calls:
            if function_to_call := available_functions.get(tool.function.name):
                # Call the search function
                search_results = function_to_call(**tool.function.arguments)
                
                if "error" in search_results:
                    if search_results["error"] == "authentication_failed":
                        return "Authentication failed. Please check your API key."
                    return f"Search error: {search_results['error']}"
                
                # Extract relevant content
                content = extract_content(search_results)
                
                if not content:
                    return "No relevant information found."
                
                # Add the search results to the conversation
                messages = [
                    {'role': 'user', 'content': query},
                    response.message,
                    {
                        'role': 'tool',
                        'name': tool.function.name,
                        'content': content
                    }
                ]
                
                # Get final response from Ollama with the search results
                final_response = await client.chat(
                    'llama3.2',
                    messages=messages
                )
                
                return final_response.message.content
    
    # If no tool calls, return the direct response
    return response.message.content

async def main():
    question = input("What would you like to know? ")
    print("\nProcessing your question...")
    answer = await process_query(question)
    print("\nAnswer:")
    print(answer)

if __name__ == "__main__":
    asyncio.run(main())