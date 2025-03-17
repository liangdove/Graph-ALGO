#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int val):val(val), next(nullptr){}
};

ListNode *detectCycle(ListNode *head){
    ListNode* fast = head;
    ListNode* slow = head;
    while(fast != NULL && fast->next != NULL){
        fast = fast->next->next;
        slow = slow->next;
        if (slow == fast){
            ListNode* index1 = slow;
            ListNode* index2 = fast;
            while (index1 != index2)
            {
                index1 = index1->next;
                index2 = index2->next;
            }
            return index2;
        }
    }
    return NULL;
}












int main(){
    ListNode* node1 = new ListNode(1);
    ListNode* node2 = new ListNode(1);
    ListNode* node3 = new ListNode(1);
    ListNode* node4 = new ListNode(1);
    node1->next = node2;
    node2->next = node3;
    node3->next = node4;
    node4->next = node2;// 创建环

    ListNode* entry = detectCycle(node1);
    if (entry != nullptr) {
        cout << "环的入口节点的值是: " << entry->val << endl;
    } else {
        cout << "链表中没有环" << endl;
    }

    // 释放链表内存
    ListNode* current = node1;
    while (current != nullptr) {
        ListNode* temp = current;
        current = current->next;
        delete temp;
    }

    return 0;
}