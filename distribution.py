#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from browser import document
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import hypergeom,binom,poisson,geom,nbinom,uniform#離散分布
from scipy.stats import norm,expon,gamma,beta,binom,cauchy,lognorm,pareto,dweibull#連続分布

#確率分布の名前とそのパラメータが入力されたらその分布を出力する．
#何個でも重ね合わせて表示できるようにする．

def decide_parameters_and_distribution(disname):
    params_lst =[]
    cont = 1
    if disname == "norm":
        while True:
            m,s = map(float,input("m:平均,s:分散:").split())
            params_lst.append([m,s])
            cont = int(input("0:終了する.それ以外の数字:続ける"))
            if cont == 0:
                break

        for param in params_lst:
            mu = param[0]
            s = param[1]
            X = np.arange(start=mu-3*s, stop=mu+3*s, step=0.1)
            norm_pdf = norm.pdf(x = X,loc = mu,scale=s)
            plt.plot(X,norm_pdf,label="mu={},sigma={}".format(mu,s))
        plt.legend()
        plt.show()
        return

    if disname == "expon":
        while True:
            lam = float(input("lam:平均"))
            params_lst.append(lam)
            cont = int(input("0:終了する:"))
            if cont == 0:
                break

        for param in params_lst:
            lam = param
            X = np.arange(start=-1, stop=15, step=0.1)
            norm_pdf = expon.pdf(x = X,loc = lam)
            plt.plot(X,norm_pdf,label="λ={}".format(lam))
        plt.legend()
        plt.show()
        return
    
    if disname == "gamma":
        while True:
            k,theta = map(float,input("k:形状,theta:尺度:").split())
            params_lst.append([k,theta])
            cont = int(input("0:終了する:"))
            if cont == 0:
                break

        for param in params_lst:
            k = param[0]
            theta = param[1]
            X = np.arange(start=-1, stop=k*(theta**2), step=0.1)
            norm_pdf = gamma.pdf(x = X,a = k,scale = theta)
            plt.plot(X,norm_pdf,label="k={},theta={}".format(k,theta))
        plt.legend()
        plt.show()
        return
    
    if disname == "beta":
        while True:
            a,b = map(float,input("a:形状母数,b:形状母数:").split())
            params_lst.append([a,b])
            cont = int(input("0:終了する:"))
            if cont == 0:
                break

        for param in params_lst:
            a = param[0]
            b = param[1]
            X = np.arange(start=0, stop=1, step=0.01)
            norm_pdf = beta.pdf(x = X,a = a,b = b)
            plt.plot(X,norm_pdf,label="a={},b={}".format(a,b))
        plt.legend()
        plt.show()
        return
    
    if disname == "cauchy":
        X = np.arange(start=-2, stop=2, step=0.1)
        norm_pdf = cauchy.pdf(x = X,)
        plt.plot(X,norm_pdf)
        plt.legend()
        plt.show()
        return
    
    if disname == "log_normal":
        while True:
            m,s = map(float,input("m:平均,s:分散:").split())
            params_lst.append([m,s])
            cont = int(input("0:終了する.それ以外の数字:続ける"))
            if cont == 0:
                break

        for param in params_lst:
            mu = param[0]
            s = param[1]
            X = np.arange(start=0, stop=mu+3*s, step=0.1)
            norm_pdf = lognorm.pdf(x = X,s = mu,scale=s)
            plt.plot(X,norm_pdf,label="mu={},sigma={}".format(mu,s))
        plt.legend()
        plt.show()
        return
    
    if disname == "cauchy":
        X = np.arange(start=-2, stop=2, step=0.1)
        norm_pdf = cauchy.pdf(x = X,)
        plt.plot(X,norm_pdf)
        plt.legend()
        plt.show()
        return
    
    if disname == "pareto":
        while True:
            a,s = map(float,input("a:平均,s:分散:").split())
            params_lst.append([a,s])
            cont = int(input("0:終了する.それ以外の数字:続ける"))
            if cont == 0:
                break

        for param in params_lst:
            mu = param[0]
            s = param[1]
            X = np.arange(start=0, stop=mu+3*s, step=0.1)
            norm_pdf = lognorm.pdf(x = X,s = a,scale=s)
            plt.plot(X,norm_pdf,label="mu={},sigma={}".format(a,s))
        plt.legend()
        plt.show()
        return

    if disname == "wible":
        while True:
            a,b = map(float,input("a:形状母数,s:経常母数:").split())
            params_lst.append([a,b])
            cont = int(input("0:終了する.それ以外の数字:続ける"))
            if cont == 0:
                break

        for param in params_lst:
            a = param[0]
            b = param[1]
            X = np.arange(start=0, stop=a+3*b, step=0.1)
            norm_pdf = lognorm.pdf(x = X,s = a,scale=b)
            plt.plot(X,norm_pdf,label="mu={},sigma={}".format(a,b))
        plt.legend()
        plt.show()
        return

#入力パート
dis_name_lst = ["norm:正規分布","expon:指数分布","gamma:ガンマ分布","beta:ベータ分布","cauchyコーシー分布","log_normal:対数正規分布","pareto:パレート分布","wible:ワイブル分布"]
#離散分布:"超幾何分布","二項分布","ポアソン分布","幾何分布","負の二項分布","一様分布",

print(dis_name_lst)
disname = input("出力したい確率分布を入力してください：")
decide_parameters_and_distribution(disname)

#一つの確率分布を決定する
#パラメータを複数変えたものをパラメータと確率を受け取る
#それを同じ画像内で表示する
#複数のパラメータの場合で重ねて表示できるようにする
