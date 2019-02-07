class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        L=[]
        for i in range(len(employees)):
            if id==employees[i].id:
                value=employees[i].importance
                L=employees[i].subordinates
        while len(L)!=0:
            tmp=L.pop()
            for j in range(len(employees)):
                if tmp==employees[j].id:
                    value=value+employees[j].importance
                    if len(employees[j].subordinates) !=0:
                        L=L+employees[j].subordinates
        return value

