class Solution(object):
    def romanToInt(self, s):
        assert 1 <= len(s) <= 15, "1 <= len(s) <= 15"
        """
        :type s: str
        :rtype: int
        """
        romantoint={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        romantoint_speical={"IV":4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
       
        integer=0

        for i in romantoint_speical:
            if i in s:
                count=s.count(i)
                integer+=count*romantoint_speical.get(i)
                s=s.replace(i,"")

        for i in s:
            if i in s:
                count2=s.count(i)
                integer+=count2*romantoint.get(i)
                s=s.replace(i,"")

        return integer
        