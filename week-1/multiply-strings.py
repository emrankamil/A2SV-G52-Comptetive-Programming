class Solution(object):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def str_to_int(string):
            str_dig=['0','1','2','3','4','5','6','7','8','9']
            integer=0
            for i in range(len(string)):
                str_num=string[i]
                int_dig=str_dig.index(str_num)
                
                integer+=int_dig*(10**(len(string)-1-i))
            return integer
        
        int_num1=str_to_int(num1)
        int_num2=str_to_int(num2)
        return str(int_num1*int_num2)