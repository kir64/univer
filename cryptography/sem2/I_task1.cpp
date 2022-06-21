#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

bool checkInput(string a, string b) {	
	string warn = "Wrong input!\n";
	for (int i = 0; i < a.size(); i++)
		if (not (a[i] >= '0' and a[i] <= '9')) {
			cout << warn;
			return false;
		}
	for (int i = 0; i < b.size(); i++)
		if (not (b[i] >= '0' and b[i] <= '9')) {
			cout << warn;
			return false;
		}
	return true;
}

void resSum(string a, string b, int k) {
	vector <int> ans; int tmp = 0;
	if (b.size() > a.size())
		swap(a, b);
	cout << a << '\n' << b << '\n';
	out << a << '\n' << b << "\n\n";
	reverse(a.begin(), a.end());
	reverse(b.begin(), b.end());
	for (int i = b.size(); i < a.size(); i++)
		b += '0';
	out << a << '\n' << b << '\n';
	for (int i = 0; i < a.size(); i++) {
		tmp = a[i] - '0' + b[i] - '0' + k;
		ans.push_back(tmp % 10);
		out << tmp << ' ' << k << '\n';
		k = tmp / 10;
	}
	if (k > 0)
		ans.push_back(k);
	reverse(ans.begin(), ans.end());
	for (int i = 0; i < ans.size(); i++)
		cout << ans[i];
	cout << endl; out << endl;
	for (int i = 0; i < ans.size(); i++)
		out << ans[i];
}

int main() {
	string a, b;
	getline(in, a);
	getline(in, b);
	if (checkInput(a, b))
		resSum(a, b, 0);
}
