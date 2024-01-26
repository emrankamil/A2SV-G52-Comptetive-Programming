class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.mp = {}
        self.life = timeToLive
        
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.mp[tokenId] = (currentTime, currentTime+self.life)
        
    def renew(self, tokenId: str, currentTime: int) -> None:
        self.mp = {key:val for key, val in self.mp.items() if currentTime<val[1]}
        
        if(tokenId in self.mp):
            self.mp[tokenId] = (currentTime, currentTime+self.life)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.mp = {key:val for key, val in self.mp.items() if currentTime<val[1]}
        return len(self.mp)
        
