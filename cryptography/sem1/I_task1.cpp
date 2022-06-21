#define forA for (int i = 0; i < 26; i++)
#define wEOF while (in.peek() != EOF) 
#define ifwEOF ifstream in("input.txt"); wEOF { in >> x; if (x >= 'A' && x <= 'Z') x = char('a' + (x - 'A')); txt.push_back(x); }
#define nl out << endl;
#define cf in.close();

#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

char c;

ifstream in("input.txt");
ofstream out("output.txt");

string alpha = "Aplhabet: ";
string choice = "Write '0' to brute force, '1' to decrypt, '2' to encrypt:\n";
string encrypt = "Encrypted text: \n";
string enter = "Enter the key:\n";
string input = "Write the text in input.txt\n";
string key = "Key = ";
string output = "Result:\n";
string text = "Text: \n";
string warning = "Wrong input!\n";

vector <char> v(26);
vector <char> a(26);
vector <int> txt;

vector <char> step(vector <char> a, int x)
{
	int j = 0;
	for (int i = x; i < 26; i++)
		v[i] = a[j++];
	j = 0;
	for (int i = 0; i < x; i++)
		v[x - 1 - i] = a[25 - i];
	return v;
}

bool checkFile(char var)
{
	if (in.peek() == EOF)
		return false;
	if (var == '0' || var == '1')
	{
		wEOF
		{
			in >> c;
			if (c != ' ' && (c < '0' || c > '9'))
				return false;
		}
		cf
	}
	else
		if (var == '2')
		{
			wEOF
			{
				in >> c;
				if (c != ' ' && (c < 'a' || c > 'z') && (c < 'A' || c > 'Z'))
					return false;
			}
			cf
		}
		else
			return false;
	return true;
}

void scan()
{
	int x;
	ifwEOF
		cf
}

void print(vector <char> v, vector <int> txt, int x)
{
	out << alpha;
	for (int i = 0; i < v.size(); i++)
		out << v[i];
	nl;
	out << key << x << endl;
	out << text;
	for (int j = 0; j < txt.size(); j++)
	{
		out << v[txt[j] % 26];
		if ((j + 1) % 20 == 0)
			nl;
	}
	nl;
}

void brute(vector <char> a, vector <int> txt)
{
	forA
	{
		out << i << ')' << endl;
		print(step(a, i), txt, i);
		nl;
	}
}

int main()
{
	char var; int key;
	cout << input << choice;
	cin >> var;
	forA
		a[i] = char('a' + i);
	if (checkFile(var))
	{
		switch (var)
		{
		case '0':
		{
			scan();
			brute(a, txt);
			break;
		}
		case '1':
		{
			scan();
			cout << enter;
			cin >> key;
			print(step(a, key), txt, key);
			break;
		}
		case '2':
		{
			vector <char> txt;
			char x;
			ifwEOF
				cout << enter;
			cin >> key;
			out << encrypt;
			step(a, key);
			map <char, int> tmp;
			forA
				tmp[v[i]] = i;
			for (int i = 0; i < txt.size(); i++)
			{
				if ((i + 1) % 20 == 0)
					nl;
				out << tmp[txt[i]] << ' ';
			}
			break;
		}
		default:
			break;
		}
	}
	else
		cout << warning;
	return 0;
}
