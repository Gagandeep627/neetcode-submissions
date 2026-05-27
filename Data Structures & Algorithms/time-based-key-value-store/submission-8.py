class TimeMap:

    def __init__(self):
        # topic : brute force->
        # initialized store= {}
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        

        # if there is no key in the store :
        # create key in the store[key] = []
        # if key not in self.store:
        #     self.store[key] = []

        # the condn.if the time stamp && VALUE is not in the store(key) rseultant array-->
        
        # if (timestamp, value) not in self.store[key]:
        # in the store[key].add -->([timestamp=1], [value=Happy])
        #     self.store[key].append((timestamp))
        #     self.store[key].append((value))

        # Topic :for binary_search operations ->
        if key not in self.store:
            self.store[key] = ([], [])

        timestamps, values = self.store[key]
        timestamps.append(timestamp)
        values.append(value)


        #Time_Complexity : O(1)
        #Space : O(m * n)
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
        
        return values[result_index]

        # topic : brute force solutions-->
        # in the store : key is not there if:
        # return "";

        # values is fetched from (store[key])
        # iterate (t, v) in values:
        # if got a condition : (t <= timestamp): (result = v) for t < timestamp too we could use the previoous results : for the value from the values
        # (val) if t > timestamp : no need to return the lower value in the values of the timestamp:
        #  if still t > timestamp : return "" empty_string;
        # else: just break : return result : resultant":

        # result = ""

        # for t,v in values:
        #     if t <= timestamp:
        #         result = v
        #     else:
        #         break


        # # Time_complexity : get() O(N) 
        # return result

        
