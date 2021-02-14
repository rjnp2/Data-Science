## Shortcomings Of Apriori Algorithm
- Using Apriori needs a generation of candidate itemsets. These itemsets may be large in number if the itemset in the database is huge.
- Apriori needs multiple scans of the database to check the support of each itemset generated and this leads to high costs.

These shortcomings can be overcome using the FP growth algorithm.

# Frequent Pattern Growth Algorithm
This algorithm is an improvement to the Apriori method. A frequent pattern is generated without the need for candidate generation. FP growth algorithm represents the database in the form of a tree called a frequent pattern tree or FP tree.

This tree structure will maintain the association between the itemsets. The database is fragmented using one frequent item. This fragmented part is called “pattern fragment”. The itemsets of these fragmented patterns are analyzed. Thus with this method, the search for frequent itemsets is reduced comparatively.

## FP Tree
Frequent Pattern Tree is a tree-like structure that is made with the initial itemsets of the database. The purpose of the FP tree is to mine the most frequent pattern. Each node of the FP tree represents an item of the itemset.

The root node represents null while the lower nodes represent the itemsets. The association of the nodes with the lower nodes that is the itemsets with the other itemsets are maintained while forming the tree.

## Frequent Pattern Algorithm Steps
The frequent pattern growth method lets us find the frequent pattern without candidate generation.

Let us see the steps followed to mine the frequent pattern using frequent pattern growth algorithm:

1) The first step is to scan the database to find the occurrences of the itemsets in the database. This step is the same as the first step of Apriori. The count of 1-itemsets in the database is called support count or frequency of 1-itemset.
2) The second step is to construct the FP tree. For this, create the root of the tree. The root is represented by null.
3) The next step is to scan the database again and examine the transactions. Examine the first transaction and find out the itemset in it. The itemset with the max count is taken at the top, the next itemset with lower count and so on. It means that the branch of the tree is constructed with transaction itemsets in descending order of count.
4) The next transaction in the database is examined. The itemsets are ordered in descending order of count. If any itemset of this transaction is already present in another branch (for example in the 1st transaction), then this transaction branch would share a common prefix to the root.

This means that the common itemset is linked to the new node of another itemset in this transaction.

5) Also, the count of the itemset is incremented as it occurs in the transactions. Both the common node and new node count is increased by 1 as they are created and linked according to transactions.
6) The next step is to mine the created FP Tree. For this, the lowest node is examined first along with the links of the lowest nodes. The lowest node represents the frequency pattern length 1. From this, traverse the path in the FP Tree. This path or paths are called a conditional pattern base.

Conditional pattern base is a sub-database consisting of prefix paths in the FP tree occurring with the lowest node (suffix).

7) Construct a Conditional FP Tree, which is formed by a count of itemsets in the path. The itemsets meeting the threshold support are considered in the Conditional FP Tree.
8) Frequent Patterns are generated from the Conditional FP Tree.

## Example Of FP-Growth Algorithm
Support Let the minimum support be 3, Confidence= 60% \
![image](https://user-images.githubusercontent.com/58425689/107868357-0b6c2880-6eac-11eb-8974-b4eaa4780a6d.png)

The above-given data is a hypothetical dataset of transactions with each letter representing an item. The frequency of each individual item is computed:- \
![image](https://user-images.githubusercontent.com/58425689/107868404-2179e900-6eac-11eb-9c3b-dc6d780f6fd7.png)

A Frequent Pattern set is built which will contain all the elements whose frequency is greater than or equal to the minimum support. These elements are stored in descending order of their respective frequencies. After insertion of the relevant items, the set L looks like this:-
### L = {K : 5, E : 4, M : 3, O : 3, Y : 3}

![image](https://user-images.githubusercontent.com/58425689/107868415-42dad500-6eac-11eb-9243-ce3d54e537db.png)

- Inserting the set {K, E, M, O, Y}:
Here, all the items are simply linked one after the other in the order of occurrence in the set and initialize the support count for each item as 1. \
![image](https://user-images.githubusercontent.com/58425689/107868421-5423e180-6eac-11eb-986a-a8a4e8e32750.png)

- Inserting the set {K, E, O, Y}:
Till the insertion of the elements K and E, simply the support count is increased by 1. On inserting O we can see that there is no direct link between E and O, therefore a new node for the item O is initialized with the support count as 1 and item E is linked to this new node. On inserting Y, we first initialize a new node for the item Y with support count as 1 and link the new node of O with the new node of Y. \
![image](https://user-images.githubusercontent.com/58425689/107868436-7c134500-6eac-11eb-8266-080c293dc7f3.png)

Similarly,

![image](https://user-images.githubusercontent.com/58425689/107868443-87ff0700-6eac-11eb-9b06-dacdaef6bec8.png)

Now, for each item, the **Conditional Pattern Base** is computed which is path labels of all the paths which lead to any node of the given item in the frequent-pattern tree. Note that the items in the below table are arranged in the ascending order of their frequencies. \
![image](https://user-images.githubusercontent.com/58425689/107868453-98af7d00-6eac-11eb-9ca3-81f764230b5e.png)

Now for each item the **Conditional Frequent Pattern Tree** is built. It is done by taking the set of elements which is common in all the paths in the Conditional Pattern Base of that item and calculating it’s support count by summing the support counts of all the paths in the Conditional Pattern Base. \
![image](https://user-images.githubusercontent.com/58425689/107868464-a8c75c80-6eac-11eb-884c-5452398f0859.png)

From the Conditional Frequent Pattern tree, the **Frequent Pattern rules** are generated by pairing the items of the Conditional Frequent Pattern Tree set to the corresponding to the item as given in the below table.
![image](https://user-images.githubusercontent.com/58425689/107868490-cbf20c00-6eac-11eb-8c7f-b5ae7ebe3be1.png)

**For each row, two types of association rules can be inferred for example for the first row which contains the element, the rules K -> Y and Y -> K can be inferred. To determine the valid rule, the confidence of both the rules is calculated and the one with confidence greater than or equal to the minimum confidence value is retained.**


