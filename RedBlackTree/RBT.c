#include<stdio.h>
#include<stdlib.h>

typedef enum {RED, BLACK} color_t;

typedef struct t_node {
    color_t color;
    int key;
    t_node *parent, *left, *right;
} t_node;

typedef struct{
    t_node *root;
    t_node *nil;
} rbtree;

rbtree *new_rbtree(void) {
    rbtree *t = (rbtree *)malloc(sizeof(rbtree));

    t_node *nil = (t_node*)malloc(sizeof(t_node));
    nil->color = BLACK;

    t->root = t->nil = nil;

    return t;
}

void exchange_color(t_node *a, t_node *b) {
    int tmp = a->color;
    a->color = b->color;
    b->color = (tmp == BLACK) ? BLACK : RED;
}

void right_rotate(rbtree *t, t_node *node) {
    t_node *parent = node->parent;
    t_node *grand_parent = parent->parent;
    t_node *node_right = node->right;

    //부모가 루트인 경우: 현재 노드를 루트로 지정(노드를 삭제한 경우만 해당)
    if(parent==t->root) t->root = node;
    else { //1-1) 노드를 grand_parent의 자식으로 연결
        if(grand_parent->left==parent) grand_parent->left = node;
        else grand_parent->right = node;
    }
    //1-2) 노드의 부모를 grand_parent로 변경(양방향 연결)
    node->parent = grand_parent;
    //2-1) parent의 부모를 노드로 변경
    parent->parent = node;
    //2-2) parent를 노드의 자식으로 연결(양방향 연결)
    node->right = parent;
    //3-1) 노드의 자식의 부모를 parent로 연결
    node_right->parent = parent;
    //3-2) 노드의 자식을 부모의 자식으로 연결(양방향 연결)
    parent->left = node_right;
}

void left_rotate(rbtree *t, t_node *node) {
    t_node *parent = node->parent;
    t_node *grand_parent = parent->parent;
    t_node *node_left = node->left;

    if(parent==t->root) {
        t->root = node;
    }
    else { //1-1) 노드를 grand_parent의 자식으로 연결
        if(grand_parent->left==parent) grand_parent->left = node;
        else grand_parent->right = node;
    }
    //1-2) 노드의 부모를 grand_parent로 변경(양뱡항 연결)
    node->parent = grand_parent;
    //2-1) parent의 부모를 노드로 변경
    parent->parent = node;
    //2-2) parent를 노드의 자식으로 변경(양방향 연결)
    node->left = parent;
    //3-1) 노드의 자식의 부모를 parent로 연결
    node_left->parent = parent;
    //3-2) 노드의 자식을 부모의 자식으로 변경(양방향 연결)
    parent->right = node_left;
}

void rbtree_insert_fixup(rbtree *t, t_node *node) {
    t_node *parent = node->parent;
    t_node *grand_parent = parent->parent;
    t_node *uncle;
    int is_left = node == parent->left;
    int is_parent_is_left;

    if(node==t->root){
        node->color = BLACK;
        return;
    }

    if(parent->color==BLACK) return;

    is_parent_is_left = grand_parent->left == parent;
    uncle = (is_parent_is_left) ? grand_parent->right:grand_parent->left;

    if(uncle->color==RED){
        parent->color = BLACK;
        uncle->color = BLACK;
        grand_parent->color = RED;
        rbtree_insert_fixup(t, grand_parent);
        return;
    }

    if(is_parent_is_left) {
        if(is_left) { //LL
            right_rotate(t, parent);
            exchange_color(parent, parent->right);
            return;
        }
        //LR
        left_rotate(t, node);
        right_rotate(t, node);
        exchange_color(node, node->right);
        return;
    }
    if(is_left){ //RL
        right_rotate(t, node);
        left_rotate(t, node);
        exchange_color(node, node->left);
        return;
    }
    //RR
    left_rotate(t, parent);
    exchange_color(parent, parent->left);
}

t_node *rbtree_insert(rbtree *t, int key){
    t_node *new_node = (t_node*)malloc(sizeof(t_node));
    new_node->key = key;
    new_node->color = RED;
    new_node->right = new_node->left = t->nil;

    t_node *current = t->root;
    while(current!= t->nil){
        if(key<current->key) {
            if(current->left == t->nil) {
                current->left = new_node;
                break;
            }
            current=current->left;
        }
        else {
            if(current->right == t->nil) {
                current->right = new_node;
                break;
            }
            current=current->right;
        }
    }
    new_node->parent = current;
    if(current==t->nil) t->root = new_node;

    //불균형 복구
    rbtree_insert_fixup(t, new_node);

    return new_node;
}

t_node *get_next_node(const rbtree *t, t_node *p) {
    t_node *current = p->right;
    if(current == t->nil) { //오른쪽에 자식이 없으면
        current = p;
        while(1) {
            //오른쪽 자식인 경우우
            if(current->parent->right==current) current = current->parent;
            //왼쪽 자식인 경우
            else return current->parent;
        }
    }
    //왼쪽 자식이 있으면
    while(current->left!=t->nil) current = current->left;
    return current;
}

void rbtree_erase_fixup(rbtree *t, t_node *parent, int is_left) {
    //삭제 후 대체한 노드가 RED(Red&Black): Black으로 변경
    t_node *extra_black = is_left ? parent->left : parent->right;
    if(extra_black->color == RED) {
        extra_black->color = BLACK;
        return;
    }

    t_node *sibling = is_left ? parent->right : parent->left;
    t_node *sibling_left = sibling->left;
    t_node *sibling_right = sibling->right;

    if(sibling->color == RED) { //[CASE D3] 형제가 RED
        if(is_left) left_rotate(t, sibling);
        else right_rotate(t, sibling);
        exchange_color(sibling,parent);
        rbtree_erase_fixup(t, parent, is_left);
        return;
    }

    t_node *near = is_left ? sibling_left : sibling_right; //형제의 자식 중 extra_black으로부터 가까운 노드
    t_node *distant = is_left ? sibling_right : sibling_right; //형제의 자식 중 extra_black으로부터 먼 노드

    //[CASE D4] 형제가 BLACK, 형제의 가까운 자식이 RED, 형제의 더 먼자식이 BLACK
    if(is_left && near->color == RED && distant->color == BLACK) {
        right_rotate(t, near);
        exchange_color(sibling, near);
        rbtree_erase_fixup(t, parent, is_left);
        return;
    }

    //[CASE D5] 형제가 BLACk, 형제의 더 먼자식이 RED
    if(is_left && distant->color == RED) {
        left_rotate(t, sibling);
        exchange_color(sibling, parent);
        distant->color = BLACK;
        return;
    }

    //[CASE D4-1] 오른쪽 노드, 형제가 BLACK, 형제의 가까운 자식이 RED, 형제의 더 먼자식이 BLACK
    if(near->color == RED && distant->color == BLACK) {
        left_rotate(t, near);
        exchange_color(sibling, near);
        rbtree_erase_fixup(t, parent, is_left);
        return;
    }
    //[CASE D5-1] 오른쪽 노드, 형제가 BLACk, 형제의 더 먼자식이 RED
    if(is_left && distant->color == RED) {
        right_rotate(t, sibling);
        exchange_color(sibling, parent);
        distant->color = BLACK;
        return;
    }

    //[CASE D2] 형제가 BLACK, 형제의 자식이 돌 다 BLACK
    sibling->color = RED;

    if(parent!=t->root) rbtree_erase_fixup(t, parent->parent, parent->parent->left == parent);
}

int rbtree_erase(rbtree *t, t_node *delete) {
    t_node *remove; //트리에서 없어질 노드
    t_node *remove_parent, *replace_node;
    int is_remove_black, is_remove_left;

    //step 1) delete 삭제 후 대체할 replace_node 찾기
    //step 1-1) delete 노드의 자식이 둘인 경우: delete의 키를 후계자의 키값으로 대체, 노드색은 delete의 색 유지
    if(delete->left!=t->nil && delete->right!=t->nil) {
        remove = get_next_node(t, delete); //후계자 노드(오른쪽 서브트리에서 가장 작은 노드)
        replace_node = remove->right; //대체할 노드 : 지워질 노드인 후계자는 항상 왼쪽 자식이 없기 때문에 자식이 있다면 오른쪽 임
        delete->key = remove->key; //delete의 키를 후계자 노드의 키값으로 대체(색은 변경 X)
    }
    else { //step 1-2) delete노드의 자식이 없거나 하나인 경우 : delete노드를 자식으로 대체, 노드색도 변경
        remove = delete;
        replace_node = (remove->right!=t->nil) ? remove->right : remove->left;
    }
    remove_parent = remove->parent;

    //step 2) remove 노드 제거하기
    //[CASE D1]: remove 노드가 루트인 경우
    if(remove==t->root) {
        t->root = replace_node; //대체할 노드를 트리의 루트로 설정
        t->root->color = BLACK; //루트 노드는 항상 BLACK
        free(remove);
        return 0; //불균형 복구 함수 호출 불필요 (제거 전 트리에서 노드가 하나 혹은 두개임으로 불균형 발생 X)
    }

    //step 2-1) 'remove의 부모'와 'remove의 자식' 이어주기
    is_remove_black = remove->color; //remove 노드 제거 전에 지워진 노드의 색 저장
    is_remove_left = remove->parent->left == remove;

    //step 2-1-1) 자식 연결
    //remove가 왼쪽 자식이었을 경우 : remove 부모의 왼쪽에 이어주기
    if(is_remove_left) remove_parent->left = replace_node;
    //remove가 오른쯕 자식이었을 경우 : remove 부모의 오른쪽에 이어주기
    else remove_parent->right = replace_node;

    //step 2-1-2) 부모도 연결(양방향 연결)
    replace_node->parent = remove_parent;
    free(remove);

    //[CASE D2~D6]: remove노두가 검정 노드인 경우
    //step 3) 불균형 복구 함수 호출
    if(is_remove_black) rbtree_erase_fixup(t, remove_parent, is_remove_left);
    return 0;
}
