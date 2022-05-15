//============================================================================
// Name        : LP2-Assign_1.cpp
// Author      : Rajas
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

//https://www.techiedelight.com/breadth-first-search/

#include <iostream>
#include <list>
#include <iterator>
#include <queue>
using namespace std;

class Graph {
public:
	int vertex, edge;
	int** adjMatrix;


public:
	Graph(int v, int e) {
		vertex = v;
		edge = e;
		adjMatrix = new int*[v];
		for (int i = 0; i < v; i++) {
			adjMatrix[i] = new int[v];
			for (int j = 0; j < v; j++){
				adjMatrix[i][j] = 0; //initialize everything to 0 initially
			}
		}
	}

	void acceptGraph() {
		int v1, v2;
		for (int i = 0; i < edge; i++) {
			cout << "Enter the edge " << i + 1 << " details:" << endl;
			cout << "Enter vertex 1:";
			cin >> v1;
			cout << "Enter vertex 2:";
			cin >> v2;
			adjMatrix[v1][v2] = 1;
			adjMatrix[v2][v1] = 1;
			cout<<endl;
		}
	}

	void displayAdjList() {
		cout<<"The Adjacency Matrix:-\n";
		for (int i = 0; i < vertex; i++) {
			for (int j = 0; j < vertex; j++) {
				cout<< adjMatrix[i][j] <<" ";
			}
			cout<<endl;
		}
	}

	void BFS(Graph const &graph, queue<int> &q, bool visited[]){

		if (q.empty()) {
			return;
		}

		// dequeue front node and print it
		int v = q.front();
		q.pop();
		cout << v << " ";

		for(int i = 0; i<vertex; i++){
			if(visited[i]==false && adjMatrix[v][i] == 1){
				visited[i] = true;
				q.push(i);
			}
		}

		BFS(graph, q, visited);
	}

	void DFS(Graph const &graph, int v, bool visited[]){
		visited[v]=true;
		// print the current node
		cout << v << " ";
		for(int i = 0; i<vertex; i++){
			if(visited[i]==false && adjMatrix[v][i] == 1){
				DFS(graph, i, visited);
			}
		}

	}

};

int main() {
	int v,e;
	cout<<"Enter number of vertices and edges (separated by space): ";
	cin>>v>>e;

	Graph g1(v, e);

	cout<<"==========================\n";
	cout<<"Note: First vertex is 0.\n";
	cout<<"==========================\n\n";

	g1.acceptGraph();
	g1.displayAdjList();

	bool visited[g1.vertex];

	//____________________________BFS________________________________
	cout<<"\nBFS:- \n";
	queue<int> q;	// create a queue for doing BFS
	for(int i=0; i<g1.vertex; i++){
		visited[i] = false;
	}

	for(int i=0; i<g1.vertex; i++){
		if(visited[i]==false){
			visited[i]=true;  // mark the source vertex as visited
			q.push(i);  // enqueue source vertex
			g1.BFS(g1, q, visited); // start BFS traversal from vertex `i`
		}
	}

	//____________________________DFS________________________________
	cout<<"\nDFS:- \n";
	//stack<int> s;    //no need of stack exclusively as recursion itself uses stack
	for(int i=0; i<g1.vertex; i++){
		visited[i] = false;
	}
	for(int i=0; i<g1.vertex; i++){
		if(visited[i]==false){
			g1.DFS(g1, i, visited); // start BFS traversal from vertex `i`
		}
	}


}
