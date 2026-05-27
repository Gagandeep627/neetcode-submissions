class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        # if key not in self.store:
        #     self.store[key] = []

        # if (timestamp, value) not in self.store[key]:
        #     self.store[key].append((timestamp))
        #     self.store[key].append((value))

        # Topic : for Binary search operations...
        if key not in self.store:
            self.store[key] = ([], [])

        timestamps, values = self.store[key]
        timestamps.append(timestamp)
        values.append(value)


        #Time_Complexity : O(1)
        # set() : O(1)

        
        

    def get(self, key: str, timestamp: int) -> str:

        
        if not key in self.store:
            return ""


        # topic : Binary_Search

        timestamps , values = self.store[key]

        low , high = 0 , len(timestamps) - 1
        result_index = -1
        # O(log(n)) --> Binary_Search_Algorithm --->
        while(low <= high):
            mid = (low + high) // 2


            if (timestamps[mid] == timestamp):
                
                return values[mid]

            elif (timestamps[mid] < timestamp):
                result_index = mid
                low = mid + 1
            else:
                high = mid - 1

        
        if (result_index == -1):
            return ""

        #Time_Complexity : O(log(n))
        #Space : O(1)
        return values[result_index]


        # result = ""

        # for t,v in values:
        #     if t <= timestamp:
        #         result = v
        #     else:
        #         break


        # # Time_complexity : get() O(N) 
        # return result

        
