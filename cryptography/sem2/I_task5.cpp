#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool isNegative = false, isEven = true, flag = false;

vector <int> lstrip(vector <int> x){
	if (x.size() > 1) {
		int k = x.size() - 1;
		while (x[k] == 0 && x.size() > 1) {
			x.pop_back();
			k--;
		}
	}
	return x;
}

vector <int> dif(vector <int> u, vector <int> v) {
	u = lstrip(u);
	v = lstrip(v);

	reverse(u.begin(), u.end());
	reverse(v.begin(), v.end());
	if (v.size() > u.size() || (v.size() == u.size() && v > u)) {
		swap(u, v);
		isNegative = true;
	}
	reverse(u.begin(), u.end());
	reverse(v.begin(), v.end());

	if (v.size() < u.size())
		for (int i = u.size() - v.size(); i > 0; i--)
			v.push_back(0);

	vector <int> w;
	int k = 0, tmp = 0;

	for (int i = 0; i < u.size(); i++) {
		tmp = u[i] - v[i] + k;
		w.push_back((tmp + 10) % 10);
		k = (tmp - 9) / 10;
	}

	for (int i = 0; i < max(u.size(), v.size()); i++)
		w.push_back(0);
	return w;
}

vector <int> add(vector <int> u, vector <int> v) {
	vector <int> w;
	int k = 0, tmp = 0;
	u = lstrip(u);
	v = lstrip(v);

	if (v.size() > u.size())
		swap(u, v);
	
	for (int i = u.size() - v.size(); i > 0; i--)
		v.push_back(0);

	for (int i = 0; i < u.size(); i++) {
		tmp = u[i] + v[i] + k;
		w.push_back(tmp % 10);
		k = tmp / 10;
	}

	for (int i = 0; i < max(u.size(), v.size()); i++)
		w.push_back(0);
	return w;
}

vector <int> mul(vector <int> u, vector <int> v) {
	if (v.size() > u.size() || (v.size() == u.size() && v > u))
		swap(u, v);
	u.push_back(0);

	int tmp = 0, k = 0;

	vector <int> w(u.size() + v.size() + 1);
	for (int i = 0; i < v.size(); i++) {
		for (int j = 0; j < u.size(); j++) {
			tmp = u[j] * v[i] + w[i+j] + k;
			w[i+j] = tmp % 10;
			k = tmp / 10;
		}
	}

	return lstrip(w);
}

vector <int> div(vector <int> u, vector <int> v)
{
	if (u[0] % 2 == 1)
		isEven = false;

	if (u.size() < v.size() || (v.size() == u.size() && v[0] > u[0])) {
		vector <int> w = { 0 };
		isNegative = true;
		return w;
	}

	vector <int> w(u.size() + 1);
	if (!isNegative) {
		int tmp, mod = 0;
		for (int i = u.size() - 1; i > -1; i--) {
			tmp = 10 * mod + u[i];
			w[i] = tmp/ v[0];
			mod = tmp % v[0];
		}
	}
	return lstrip(w);
}

vector <int> mod(vector <int> u, vector <int> v)
{
	vector <int> hlp;
	bool flag1 = false, flag2 = false;
	if (u[0] == '0' && u.size() == 1) {
		hlp.push_back(0);
		flag1 = true;
		return hlp;
	}

	reverse(u.begin(), u.end());
	reverse(v.begin(), v.end());
	if (u.size() < v.size() || (v.size() == u.size() && v > u)) {
		flag2 = true;
		reverse(u.begin(), u.end());
		return u;
	}
	reverse(u.begin(), u.end());
	reverse(v.begin(), v.end());

	vector <int> ans;
	vector <int> Q(u.size());
	vector <int> w(u.size() + 1);
	int cur = 0, m = 0, d = 0, mod = 0, q = 0, r = 0, tmp = 0;

	if (! (flag1 && flag2)) {
		if (v.size() == 1) {
			for (int i = u.size() - 1; i > -1; i--) {
				cur = 10 * mod + u[i];
				w[i] = cur / v[0];
				mod = cur % v[0];
			}
			hlp.push_back(mod);
			return hlp;
		}

		else {
			d = 10 / (v[v.size() - 1] + 1);
			vector <int> D = { d };
			u = mul(u, D);
			v = mul(v, D);

			if (u.size() - v.size() + v.size() > u.size() - 1)
				u.push_back(0);
			for (int i = m; i > -1; i--) {
				tmp = u[i + v.size()] * 10 + u[i + v.size() - 1];
				q = tmp / v[v.size() - 1];
				r = tmp % v[v.size() - 1];

				do {
					if (q == 10 || q * v[v.size() - 2] > 10 * r + u[i + v.size() - 2])
						q--;
					r += v[v.size() - 1];

				} while (r < 10);

				vector <int> Q1;
				Q1.push_back(q);

				int s = i + int(v.size());
				vector <int> u1(v.size() + 1);
				vector <int> difference(v.size() + 1);

				for (int j = s; j > i-1; j--)
					u1[j - i] = u[j];

				vector <int> b;
				for (int j = 0; j < v.size() + 1; j++)
					b.push_back(0);
				b.push_back(1);

				difference = dif(u1, mul(Q1, v));
				if (flag)
					difference = dif(b, difference);

				Q[i] = q;
				if (flag) {
					Q[i]--;
					difference = add(v, difference);
					flag = false;
				}

				for (int j = s; j > i-1; j--)
					u[j] = difference[j - i];
			}

			Q = lstrip(Q);

			vector <int> q1;
			for (int i = v.size() - 1; i > -1; i--)
				q1.push_back(u[i]);
			reverse(q1.begin(), q1.end());

			vector <int> hlp(q1.size());
			for (int i = q1.size() - 1; i > -1; i--) {
				cur = 10 * mod + q1[i];
				hlp[i] = cur / D[0];
				mod = cur % D[0];
			}
			ans = lstrip(hlp);
		}
	}
	return ans;
}

vector <int> pow(vector <int> u, vector <int> v, vector <int> m) {
	vector <int> w(u.size() + v.size() + 1);
	vector <int> N = v, Z = u, del = { 2 }, Y = { 1 }, tmp;

	while (true) {
		N = div(N, del);
		tmp = mul(Z, Z);
		if (isEven)
			Z = mod(tmp, m);
		else {
			Y = mod(mul(Y, Z), m);
			if (N.size() == 1 && N[0] == 0)
				break;
			Z = mod(tmp, m);
			isEven = true;
		}
	}
	Y = lstrip(mod(Y, m));
	reverse(Y.begin(), Y.end());

	return Y;
}

bool check(string s) {
	for (int i = 0; i < s.size(); i++)
		if (s[i] < '0' || s[i] > '9')
			return 0;
	return 1;
}

vector <int> convert(string s) {
	vector <int> v;
	for (int i = 0; i < s.size(); i++)
		v.push_back(atoi(s.substr(i, 1).c_str()));
	reverse(v.begin(), v.end());
	return v;
}

int main() {
	vector <int> u, v, m, ans;
	string s1, s2, s3;
	set <char> tmp;

	cout << "Enter x, y and mod:" << endl;
	getline(cin, s1);
	getline(cin, s2);
	getline(cin, s3);
	for (int i = 0; i < s3.size(); i++)
		tmp.insert(s3[i]);

	if (!(check(s1) && check(s2) && check(s3))) {
		cout << "Wrong input!" << endl;
		return 0;
	}
	else if (tmp.find('0') != tmp.end() && tmp.size() == 1){
		cout << "Zero division" << endl;
		return 0;
	}
	u = convert(s1), v = convert(s2), m = convert(s3);
	ans = pow(u, v, m);

	cout << "Result: ";
	for (int i = 0; i < ans.size(); i++)
		cout << ans[i];
	cout << endl;
}
