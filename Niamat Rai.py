import numpy
import xlrd
import math

dist_l, dist_q, dist_c= 0,0,0
l =[]
rowmin, rowmax = 0, 8
book = xlrd.open_workbook("python.xlsx")
sh = book.sheet_by_index(0)
def distfrom(x0,y0,x1,y1):
  r = float((((x1 - x0)/0.01)**2.0)+ (float(y1)- y0)**2.0)**(1.0/2)
  return r

def xl(i):
  return[float(sh.cell_value(rowx=i, colx=0)), float(sh.cell_value(rowx=i, colx=1))]    #import sheet qand excel file. sh = sheet.

def linear(m,c):
  global dist_l
  for i in range(0,rowmax+1):
         x0 = float(xl(i)[0])
         y0 = float(xl(i)[1])
         dist = float(math.fabs((y0-m*x0-c)/((1+m**2)**(0.5))))
         dist_l+= dist
  return dist_l
def quaddist(a,b,c):
  global dist_q
  for i in range(0,rowmax+1):
        n = []
        x0 = xl(i)[0]
        y0 = xl(i)[1]
        c0 = 2*(a**2)
        c1 = 3*b*a
        c2 = (b**2)+ 2*a*c - 2*a*y0 + 1
        c3 = c*b - b*y0 - x0
        p = [c0, c1, c2, c3]
        root = numpy.roots(p)
        print root
        k = root[2]
        j = (a*(k)**2)+ (b*(k))+ (c)
        dist_q += distfrom(x0,y0,k,j)
        
  return dist_q

def cubicdist(a,b,c,d):
  global dist_c
  for i in range(0,rowmax+1):
          n = []
          x0 = xl(i)[0]
          y0 = xl(i)[1]
          c0 = 3.0*(a**2)
          c1 = 5.0*a*b
          c2 = 4.0*a*c + 2.0*(b**2)
          c3 = 3.0*b*c - 3.0*a*y0 + 3*a*d
          c4 = 1.0*c**2 - 2.0*b*y0 + 1.0 + 2*b*d
          c5 = -1.0*c*y0 - 1.0*x0 + 1.0 *d*c
          p = [c0,c1,c2,c3,c4,c5]
          root = numpy.roots(p)
          for i in root:
            if numpy.isreal(i) == True:
              k = i
              j = float((1.0*a*(k)**3)+ (1.0*b*(k)**2)+ (1.0*c*(k))+ (d))
              n = (distfrom(x0,y0,k,j))
              print k, j
              dist_c += n
          """k = root[0]
          j = float((a*(k)**3)+ (b*(k)**2)+ (c*(k))+ (d))
          print k, j
          n.append(distfrom(x0,y0,k,j))
          k = root[3]
          j = float((a*(k)**3)+ (b*(k)**2)+ (c*(k))+ (d))
          n.append(distfrom(x0,y0,k,j))
          k = root[4]
          j = float((a*(k)**3)+ (b*(k)**2)+ (c*(k))+ (d))
          n.append(distfrom(x0,y0,k,j))
          dist_c += min(n)
          print n
          print dist_c"""
  return dist_c
#print cubicdist(7.701228387*(10**-4), - 0.200286475, 17.35250396, - 499.6424141)
print quaddist(-0.0013,0.2275,-8.4691)
#print linear(-0.0034,1.4778)
