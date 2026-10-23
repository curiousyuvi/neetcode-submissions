class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        
        bounded_strs=[f"[s]{x}[e]" for x in strs]
        return "[,]".join(bounded_strs)

    def decode(self, s: str) -> List[str]:
        if s=="":
            return []
        
        bounded_strs=s.split("[,]")
        return [x.replace("[s]","").replace("[e]","") for x in bounded_strs]
