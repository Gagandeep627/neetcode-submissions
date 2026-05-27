class Solution:
    def isPalindrome(self, s: str) -> bool:



        # topic : 2 pointers -- approach -->
        original_s = list(s)

        reverse_s = original_s[::-1]


        original_s = "".join(i for i in original_s if i.isalnum())


        reverse_s = "".join(i for i in reverse_s if i.isalnum())


        # print(original_s)

        # print(reverse_s)


        return (original_s.lower() == reverse_s.lower())




        