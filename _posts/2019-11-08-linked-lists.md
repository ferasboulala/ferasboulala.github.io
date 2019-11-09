---
layout: post
title: "Intrusive Linked Lists"
---

I have just recently made an interesting discovery on an alternative way of representing linked lists and thought I would share how clever it is. I feel a bit ashamed that I did not hear about this sooner but better late than never! They are called _intrusive linked lists_.

Assuming we are coding in C or C++, generally, when implementing linked lists, one would rely on the power of macros or templates to abstract types. It is also possible to abstract types with raw pointers to hold the data but that comes with the cost of an extra indirection which may affect performance. Until now, I did not know any other way of creating a convenient, type abstracted linked list (if you hate macros, templates and raw pointers, you could even go as far as defining an opaque structure with a size field but it is way too ugly for my liking).

Essentially, the goal of these methods was to define some kind of structure that would hold a pointer to anoter same structure. That would make this chain a linked list. It would look a little bit like this:
```cpp
template<typename T>
struct ListNode {
    T data;
    Node *next;
    Node *prev;
};
```

But there is a fundamental flaw with this approach: it strongly assumes lists should point to the same type that holds them whereas in reality, the only requirement to have a linked list would be to somehow connect objects and have a way of deleting and ading more objects in the chain. In a way, linked lists already use indirection and that assumptions did not take advantage of it.

Intrusive linked lists, on the other hand, aim to define a simple structure that will be embedded inside a user structure (hence the name). It does precisely what a linked list is supposed to do: act like a pointer.
```c
// Simple list structure that is meant to be embedded into a user struct.
struct list {
    struct list *next;
    struct list *prev;
};

// User defined structure
struct UserStruct {
    int data
    size_t len;
    ...
    struct list list;
    ...
};
```

This representation has several advantages:
1. Firstly, we achieve type abstraction without the use of macros (they're highly inconvenient) or templates (if you're stuck with C). The only macro required for this kind of list is the _offsetof_ which is already provided by _gcc_. This is necessary to get the data associated with a list node. An implementation would look like:
```c
#define offsetof(name, type) (&((type*)0)->name))
```

2. Secondly, because it does not rely on macros nor templates to redefine every procedure for every type, the code size is generally smaller. This could be useful for very restricted systems. Such procedures involve the initialization of the list and add and remove operations.
```c
void list_add(struct list *parent, struct list *child)
{
    if (parent->next)
    {
        parent->next->prev = child;
    }
    child->next = parent->next;
    parent->next = child;
    child->prev = parent;
}
```
3. Futhermore, This kind of representation could be applied to any pointer based data structure like trees or graphs. The only downside is that if there is ever a requirement to sort or operate on the data, comparators will not be inlined.
4. Finally, it is possible to have a heterogeneous list because the type is, again, not assumed with this representation. The type identifier must be at a constant offset from the list structure in this case. Alternatively, the list structure could be set as the first field of the list node (an offset of 0 bytes).
```c
struct UserStruct {
    struct list list;
    int type_id;
    ...
};
```

I was made aware of this when I stumbled upon Linux data structures. Unlike C++, C does not have a standard library for general purpose data structures and algorithms (you could always use _gnulib_ but that comes at a very strong assumptions that you are using _autotools_. _glib_ is a good choice though.) and so I wondered how did the kernel writers achieve anything down there.

