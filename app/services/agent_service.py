from app.agents.document_agent import agent 


class AgentService : 

    @staticmethod
    def run(question : str):
        
        result = agent.invoke(
            {
                "question":question,
                "context" :"",
                "answer":"",
                "route":"",
                "tool_result":""
            }
        )

        return result