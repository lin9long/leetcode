#!/usr/bin/python
# -*-coding:utf-8 -*-

from typing import List


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:

    def getImportance(self, employees: List[Employee], id: int) -> int:
        s_employees = set(employees)
        def get(employees, id: int, i_l=[]):
            if employees:
                for i in employees:
                    if i.id == id and id is not None:
                        i_l.append(i.importance)
                        for j in i.subordinates:
                            get(employees, j, i_l)
            return i_l

        return sum(get(s_employees, id))
