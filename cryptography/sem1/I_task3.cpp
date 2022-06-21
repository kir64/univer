#define forA for (int i = 0; i < 26; i++)
#define forV for (int i = 0; i < v.size(); i++)
#define wEOF while (in.peek() != EOF) 
#define ifwEOF wEOF { in >> c; if (c >= 'A' && c <= 'Z') c = char('a' + (c - 'A')); v.push_back(c); }

#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>
#include <vector>
#include <map>
#include <set>

using namespace std;

char c;
string s;
string hlp = "etaoinshrdlcumwfgypbvkxjqz";
string choice = "Enter here 0 to decrypt or 1 to encrypt.";
string input0 = "Enter encrypted text in 'input.txt'.\n";
string input1 = "Enter key here and text to encrypt in 'input.txt'. ";
string output = "Result: ";
string warning = "Wrong input!";

vector <char> v;
vector <pair <string, int>> b;
vector <pair <string, int>> t;

map <char, char> x;

ifstream in("input.txt");
ofstream out("output.txt");

bool check()
{
	wEOF
	{
		in >> c;
		if (c != ' ' && (c < 'a' || c > 'z') && (c < 'A' || c > 'Z'))
			return false;
	}
	return true;
}

bool cmpC(pair <char, float> a, pair <char, float> b)
{
	return (a.second > b.second);
}

bool cmpS(pair <string, float> a, pair <string, float> b)
{
	return (a.second > b.second);
}

void brute(set <string> s, vector <pair <string, int>> v, string txt, int l)
{
	int cnt = 0; int k = 0;
	string tmp = txt;
	for (auto i : s)
	{
		k = tmp.find(i);
		while (k != -1)
		{
			cnt++;
			tmp = tmp.substr(k + l);
			k = tmp.find(i);
		}
		v.push_back(make_pair(i, cnt));
		cnt = 0; tmp = txt;
	}
	sort(v.begin(), v.end(), cmpS);
	forV
		out << v[i].first << " - " << v[i].second << endl;
	out << endl;
}

void print(map <char, char> x, vector <char> v)
{
	forV
	{
		if ((i + 1) % 40 == 0)
			cout << endl;
		cout << x[v[i]];
	}
	cout << endl;
}

void stat()
{
	vector <int> alph(26);
	vector <pair <char, float>> p(26);
	ifstream in("input.txt");
	ifwEOF
	int n = v.size();
	string txt = "";
	forV
		txt += v[i];
	forV
		alph[v[i] - 'a']++;
	forA
		p[i] = make_pair(char('a' + i), float(alph[i]) / n * 100);
	sort(p.begin(), p.end(), cmpC);
	string s2 = "";
	string s3 = "";
	set <string> bi;
	set <string> tri;
	for (int i = 0; i < n - 2; i++)
	{
		s2 = v[i]; s2 += v[i + 1];
		s3 = s2 + v[i + 2];
		bi.insert(s2);
		tri.insert(s3);
	}
	if (n > 2)
	{
		s2 = v[n - 2]; s2 += v[n - 1];
		bi.insert(s2);
	}
	forA
		out << p[i].first << " - " << p[i].second << endl;
	brute(bi, b, txt, 2);
	brute(tri, t, txt, 3);
}

int main()
{
	cout << choice << endl;
	int var; cin >> var;
	if (check())
	{
		switch (var)
		{
			case 0:
			{
				cout << input0 << endl;
				stat();
				for (char i = 'a'; i <= 'z'; i++)
					x[i] = '*';
				x['n'] = 't'; x['d'] = 'h'; x['q'] = 'e'; //ndq
				x['m'] = 'a'; x['y'] = 'n'; x['i'] = 'd'; //myi
				x['p'] = 'o'; //on, o
				x['r'] = 'r'; //her
				x['j'] = 'y'; x['s'] = 'u'; //jps, jp, ps
				x['z'] = 's'; // ?tore
				x['h'] = 'm'; //many? - some!
				x['k'] = 'i'; //Is
				x['b'] = 'f'; //oF 
				x['a'] = 'p'; x['v'] = 'l'; //people
				x['f'] = 'x'; // siXteen
				x['u'] = 'b'; //numBer
				x['g'] = 'k'; //sKin
				x['l'] = 'c'; //Company, musCle
				x['t'] = 'g'; //stronG
				x['o'] = 'w'; //Was
				cout << output << endl;
				print(x, v);
				break;
			}
			case 1:
			{
				cout << input1 << endl;
				getline(cin, s); getline(cin, s);
				for (int i = 0; i < s.size(); i++)
					x[char('a' + i)] = s[i];
				cout << endl << output << endl;
				ifstream in("input.txt");
				ifwEOF
				print(x, v);
				break;
			}
			default:
				break;
		}
	}
	else
		cout << warning << endl;
	return 0;
}
