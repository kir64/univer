#define isDigit if (not (a[i] >= '0' and a[i] <= '9')) {cout << warn; return false; }

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

void normalize(string &a, string &b)
{
	if (b.size() > a.size())
		swap(a, b);
	reverse(a.begin(), a.end());
	reverse(b.begin(), b.end());
}

void print(vector <string> ans) 
{
	for (int i = 0; i < ans.size(); i++)
		cout << ans[i] << endl;
	cout << endl;
}

bool checkInput(string a, string b) 
{
	string warn = "Wrong input!\n";
	for (int i = 0; i < a.size(); i++)
		isDigit
	for (int i = 0; i < b.size(); i++)
		isDigit
	return true;
}

string standard(string ans) 
{
	int flag = -1, i = 0;
	while (ans[i] == '0' and i < ans.size() - 1)
		flag = i++;

	if (flag != -1)
		ans.erase(ans.begin(), ans.begin() + flag + 1);
	return ans;
}

string resSum(string a, string b) 
{
	string ans = "";
	normalize(a, b);
	for (int i = b.size(); i < a.size(); i++)
		b += '0';
	int tmp = 0, k = 0;
	for (int i = 0; i < a.size(); i++) {
		tmp = a[i] - '0' + b[i] - '0' + k;
		ans += char('0' + tmp % 10);
		k = tmp / 10;
	}
	if (k > 0)
		ans += char('0' + k);
	reverse(ans.begin(), ans.end());
	return ans;
}

string resDif(string a, string b) {
	normalize(a, b);
	for (int i = b.size(); i < a.size(); i++)
		b += '0';

	int k = 0, i = 0, tmp;
	string ans = "";
	
	while (i < a.size()) {
		tmp = a[i] - b[i] + k;
		if (tmp < 0) {
			k = -1;
			tmp += 10;
		}
		else
			k = 0;
		ans += char('0' + tmp % 10);
		i += 1;
	}

	reverse(ans.begin(), ans.end());
	return standard(ans);
}

string resMul(string u, string v) 
{
	normalize(u, v);
	u += '0';

	vector <int> w(u.size() + v.size());
	int k = 0, t = 0;
	for (int i = 0; i < v.size(); i++)
		for (int j = 0; j < u.size(); j++) {
			t = (v[i] - '0') * (u[j] - '0') + w[i + j] + k;
			w[i + j] = t % 10;
			k = t / 10;
		}
	
	reverse(w.begin(), w.end());

	string ans = "";
	for (int i = 0; i < w.size(); i++)
		ans += char('0' + w[i]);
	
	
	return standard(ans);
}

int main() 
{
	string a, b;
	getline(cin, a);
	getline(cin, b);
	if (checkInput(a, b))
		cout << resMul(a, b) << endl;
}
