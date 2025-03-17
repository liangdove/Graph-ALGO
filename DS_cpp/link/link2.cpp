#include <iostream>

using namespace std;

//反转链表
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int val):val(val), next(nullptr){}
};

ListNode* reverseList(ListNode* head){
    ListNode* temp;
    ListNode* cur = head;
    ListNode* pre = NULL;
    while (cur)
    {
        temp = cur->next;
        cur->next = pre;
        pre = cur;
        cur = temp;
    }
    return pre;
}

//f反转链表递归写法
ListNode* reverse(ListNode* pre, ListNode* cur);

ListNode* reverseListRecur(ListNode* head){
    return reverse(NULL, head);
}

ListNode* reverse(ListNode* pre, ListNode* cur){
    if(cur == NULL){
        return pre;
    }
    ListNode* temp = cur->next;
    cur->next = pre;
    return reverse(cur, temp);
}

//交换链表的相邻节点
ListNode* swapPairs(ListNode* head){
    ListNode* dummyHead = new ListNode(0);
    dummyHead->next = head;
    ListNode* cur = dummyHead;
    while (cur->next != nullptr && cur->next->next != nullptr){
        ListNode* tmp = cur->next;
        ListNode* tmp1 = cur->next->next->next;

        cur->next = cur->next->next;
        cur->next->next = tmp;
        cur->next->next->next = tmp1;

        cur = cur->next->next;
    }
    ListNode* result = dummyHead->next;
    delete dummyHead;
    return result;
}

//删除倒数第n个节点，双指针应用
ListNode* removeNthFromEnd(ListNode* head, int n){
    ListNode* dummyHead = new ListNode(0);
    dummyHead->next = head;
    ListNode* slow = dummyHead;
    ListNode* fast = dummyHead;
    while (n-- && fast != NULL)
    {
        fast = fast->next;
        slow = slow->next;
    }
    slow->next = slow->next->next;

    return dummyHead->next;
}

//相交的链表节点
ListNode *getIntersextionNode(ListNode *headA, ListNode *headB){
    ListNode *curA = headA;
    ListNode *curB = headB;
    int lenA = 0, lenB = 0;

    while(curA != NULL){
        lenA++;
        curA = curA->next;
    }
    while(curB != NULL){
        lenB++;
        curB = curB->next;
    }

    curA = headA;
    curB = headB;

    if(lenB > lenA){
        swap(lenA, lenB);
        swap(curA, curB);
    }

    int gap = lenA - lenB;

    while(gap--){
        curA = curA->next;
    }

    while(curA != NULL){
        if(curA == curB){
            return curA;
        }
        curA = curA->next;
        curB = curB->next;
    }

    return NULL;
}

ListNode *createList(int arr[], int n){
    if(n == 0)return NULL;
    ListNode *head = new ListNode(arr[0]);
    ListNode *cur = head;
    for(int i = 1; i < n; i++){
        cur->next = new ListNode(arr[i]);
        cur = cur->next;
    }
    return head;
}

// 连接两个链表，使它们相交
void connectLists(ListNode* listA, ListNode* listB, int pos) {
    if (pos == -1) return;
    ListNode* curA = listA;
    for (int i = 0; i < pos; i++) {
        curA = curA->next;
    }
    ListNode* curB = listB;
    while (curB->next != NULL) {
        curB = curB->next;
    }
    curB->next = curA;
}

// 打印链表
void printList(ListNode* head) {
    ListNode* cur = head;
    while (cur != NULL) {
        std::cout << cur->val << " ";
        cur = cur->next;
    }
    std::cout << std::endl;
}

// 测试程序
int main() {
    // 创建链表 A
    int arrA[] = {1, 2, 3, 4, 5};
    int nA = sizeof(arrA) / sizeof(arrA[0]);
    ListNode* headA = createList(arrA, nA);

    // 创建链表 B
    int arrB[] = {6, 7};
    int nB = sizeof(arrB) / sizeof(arrB[0]);
    ListNode* headB = createList(arrB, nB);

    // 使链表 B 与链表 A 在第 2 个节点（索引从 0 开始）相交
    connectLists(headA, headB, 2);

    // 打印链表 A 和 B
    std::cout << "List A: ";
    printList(headA);
    std::cout << "List B: ";
    printList(headB);

    // 调用查找相交节点的函数
    ListNode* intersection = getIntersextionNode(headA, headB);
    if (intersection != NULL) {
        std::cout << "Intersection node value: " << intersection->val << std::endl;
    } else {
        std::cout << "No intersection found." << std::endl;
    }

    return 0;
}


