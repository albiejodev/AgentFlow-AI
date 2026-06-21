from app.agents.document_agent import agent 


class AgentService : 

    @staticmethod
    def run(session_id:str , question : str):
        
        result = agent.invoke(
            {
                "session_id":session_id,
                "history":"",
                "question":question,
                "context" :"",
                "answer":"",
                "route":"",
                "tool_result":""
            }
        )

        return result