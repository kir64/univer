#define fori3 for (int i = 0; i < 3; i++) 
#define forj3 for (int j = 0; j < 3; j++)
#define forl3 for (int l = 0; l < 3; l++)
#define wEOF while (in.peek() != EOF)
#define ifwEOF wEOF { in >> c; if (c >= 'A' && c <= 'Z') c = char('a' + (c - 'A')); txt.push_back(c); }
#define warn cout << warning;

#include <iostream>	
#include <vector>
#include <fstream>
#include <string>
#include <map>

using namespace std;

typedef vector <vector <int>> matrix;

string warning = "Wrong input!\n";
string choice = "Enter 0 to decrypt or 1 to encrypt.\n";
string input = "Enter key-word and your text in 'input.txt'.\n";

string alph = "abcdefghijklmnopqrstuvwxyz";
matrix K{ {6, 24, 1}, {13, 16, 10}, {20, 17, 15} };
matrix _K{ {8, 5, 10}, {21, 8, 21}, {21, 12, 8} };

char c;

ifstream in("input.txt");
ofstream out("output.txt");

void print(matrix &v)
{
	fori3
	{
		forj3
			cout << v[i][j] << ' ';
		cout << endl;
	}
	cout << endl;
}

matrix mul(matrix a, matrix b)
{
	matrix tmp(vector <vector <int>>(3, vector <int>(3)));
	fori3
		forj3
		forl3
		tmp[i][j] += a[i][l] * b[l][j];
	fori3
		forj3
		tmp[i][j] %= 26;
	return tmp;
}

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

int main()
{
	cout << choice;
	int var; cin >> var;
	cout << input;
	string key; getline(cin, key);
	getline(cin, key);
	map <char, int> hlp;
	for (int i = 0; i < alph.size(); i++)
		hlp[alph[i]] = i;
	if (check() && hlp.size() == 26)
	{
		vector <char> txt;
		ifstream in("input.txt");
		switch (var)
		{
		case 0:
		{
			ifwEOF
				for (int i = 0; i < txt.size(); i++)
					txt[i] = alph[(hlp[txt[i]] + 26 - hlp[key[i % 3]]) % 26];
			//
			for (int i = 0; i < txt.size(); i++)
			{

				if (i % 9 == 0)
					cout << endl;
				cout << txt[i];
			}
			cout << endl;
			//
			vector <matrix> ans(ceil(txt.size() / 9.), matrix(vector <vector <int>>(3, vector <int>(3))));
			for (int i = 0; i < txt.size(); i++)
				ans[i / 9][(i % 9) / 3][i % 3] = hlp[txt[i]];
			//
			for (int i = 0; i < ans.size(); i++)
				print(ans[i]);
			//
			for (int i = 0; i < ans.size(); i++)
				ans[i] = mul(ans[i], _K);
			//
			for (int i = 0; i < ans.size(); i++)
				print(ans[i]);
			//
			int cnt = 0;
			for (int i = 0; i < ans.size(); i++)
			{
				forj3
					forl3
				{
					cnt++;
					if (cnt <= txt.size())
						out << alph[ans[i][j][l]];
					else
						break;
				}
				out << endl;
			}
			break;
		}
		case 1:
		{
			ifwEOF
				vector <matrix> ans(ceil(txt.size() / 9.), matrix(vector <vector <int>>(3, vector <int>(3))));
			for (int i = 0; i < txt.size(); i++)
				ans[i / 9][(i % 9) / 3][i % 3] = hlp[txt[i]];
			//
			for (int i = 0; i < ans.size(); i++)
				print(ans[i]);
			//
			for (int i = 0; i < ans.size(); i++)
				ans[i] = mul(ans[i], K);
			//
			for (int i = 0; i < ans.size(); i++)
				print(ans[i]);
			//
			for (int i = 0; i < ans.size(); i++)
				forj3
				forl3
				ans[i][j][l] = (hlp[key[l]] + ans[i][j][l]) % 26;
			//
			for (int i = 0; i < ans.size(); i++)
				print(ans[i]);
			//
			int cnt = 0;
			for (int i = 0; i < ans.size(); i++)
			{
				forj3
					forl3
				{
					cnt++;
						if (cnt <= ceil(txt.size() / 3.) * 3)
							out << alph[ans[i][j][l]];
						else
							break;
				}
				out << endl;
			}
			break;
		}
		default:
			warn
				break;
		}
	}
	else
		warn
		return 0;
}
