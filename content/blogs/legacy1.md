---
title: 첫 글
date: 2022-07-21
draft: false
github_link: https://github.com/ryuzu3747
author: RyuZU
tags:
  - Markdown
  - syntax
image: 
description: ""
---
  

저키로 처음 블로그를 만들어보았다

  

마크다운도 처음써보는데 신기하다

  

```c++

#include <bits/stdc++.h>

#define ll long long int

#define swap(a,b) {ll c; c=a;a=b;b=c;}

#define MOD 1000000007

#define pii pair<int,int>

#define iii tuple<int,int,int>

using namespace std;

  

ll multi(ll i,ll k){

    if(k==1) return i;

    if(k==0) return 1;

    if(k%2==1) return ((i*multi(i,k/2))%MOD*multi(i,k/2))%MOD;

    else return (multi(i,k/2)*multi(i,k/2))%MOD;

}

  

int main(){

    int n,k,a[2001];

    cin>>n>>k;

    for(int i=0;i<n;i++) cin>>a[i];

    ll setsu = 1;

    for(int i=0;i<k-1;i++){

        setsu = (setsu*2)%MOD;

    }

    ll ncrtop = 1, ncrbot = 1;

    for(int i=0;i<k;i++){

        ncrtop = (ncrtop*(n-i))%MOD;

        ncrbot = (ncrbot*(i+1))%MOD;

    }

    ll div = (ncrtop*multi(ncrbot,MOD-2))%MOD;

    cout<<(setsu*div)%MOD;

}

```

신기하지 않은가?? 아닌가??

  

> 이런것도 된다!

  

* 이것도 있다...