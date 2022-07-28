# -*- coding: utf-8 -*-
"""Dicoding_MachineLearningTerapanProject1 (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RheWqeG2ZnMvIe7xDo_aZJ6UPJmnzn9o

Menambahkan Library yang diperlukan
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline
import seaborn as sns

"""Muat dataset langsung secara daring"""

# load the dataset
url = 'https://raw.githubusercontent.com/tidyverse/ggplot2/main/data-raw/economics.csv'
economics = pd.read_csv(url, header=None)
economics

"""![Metadata variable about economics usa dataset](data:image/png;base64,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+69TJZXyWuWRO07iJeCkOzhS5MHJBOBua17H4LJ25GLTmOwtP3jWyzOZv0a6juTwnDEo077GcMZQiI+I1cS52lpCiDarBvlTDz1dF7IE3n6+DdNrak6Wv9+OAafvzD/CQ1SbcPEZ7t7YPBbHRoE4X4JE5Lc12jeJaHNYTuMMvK4BIiIHCxREVD05iJFdkERURN27PIiIiGj7YQsFERERhcYCBREREYXGAgURERGFxgIFERERhcYCBREREYXGAgURERGFFupno5cuXdJTREREtJ3x36EgIiKi0NjlQURERKGxQEFEREShsUBBREREobFAQURERKGxQEFEREShsUBBREREobFAQURERKGxQEFEREShsUBBREREoW3fAsX8KKLxNFb1LNFGWByLIjq2qOfuhEWMRqMYndezm9Yq0vGtkE4icrCFgmhbaUZ/JoP+Fj1LRFQndS9QrE712TUuu+YlakLy46tlLKfRp7+Xn74ps41A1UqcZebyYjU551h6zr+t2fogjynm006aTr6IhgP/GzDehfboqKiz0ZZix5C4brKVybnewVq+uUx8zBiUsTQ65cRhH9LLOpbc9dV3nkBsmcfSaUmb2wdavsx7oWD7ctblXvG3UMh1+0ReyO+c/ZS+X/V5GufnP7fS95I8vnkcdYxS5yC/b0fXKeArBxqM8y5zjxPRxpP/c7B6WknH5f9sLB9Pr6gvrk/mPy3mR+bkzEJ+xLL0tGTOr+Qne628lVywl0hqX5/JT14XM3MjecsaEVs41Prmtu4xhYWksS+RhpiZJknur3dSbElbjrieJ8T19K5fIHaCsSLW70KXiiPBjg1zeXB933wwLgPzTlrc5SqmnVizj2XGmdi3vD+ce8AXpz7rda/49yuPDxx180bux9vWfy7yXI8a+W6va5xbcN6k0vc77nGcNJU8B1+aJTVf8h4nog23Ll0e4qGCwY5GNdPUiReTFiZeL1Z3MZtfG9E5lkEm3mwvkRqfakMM96mZljZ0YwIzTu1p+QJmLnajTW47P45hJLxjCs3xFLrPnlE1zXtv4318Hm1Pectpa7uBHiROdoqokUTsxLqBszOihixqsakJdJ/uF9GliRg8nd6L4VeNGOxp85YHtfQjk9Hby9gScZZy41Ic62QCT/R9zY2tGyK2Eked5c1o6wFmL19Vc3ER02NOOgURx+IlrWdqUad7pQgr+QI6m9S03M+T2Sxy8tzmZzBx0LivRD6+IO7lUho7kv5zDbB6P4ND+jgVzyGo0j1ORBtufcZQ7Iv4Hip7Hm8FlnLiUd+MY4OtmDihmyxLNP06zagNu7sw9dBO/a16UDsFk9U3ZjCrXwqrV3LInpLdF3q/9icmHqmm2/pvuhvssg4g4r6chEcj4kW4KF6EV3Hp1DsYONBgxEIU7UOzesUiWo4hcXACMb2u2eQvYwsHI9ij521NERywHsGte/V8FbHldanEMHAlq78tZ33ulWrcFo+FvHiv3/ov3yp+L2uNHcfRfXFY33fBbqLqFT8Hv+rucSLaSHd8UKZdixE1rcxpWaOM2Q8GX9+vmI8tJTAt1slfn8Qz792wl0nNT3u10AvnZ9H9tPeIlK0icht73+4nqWpeNzn2dDu5jasYmcsHYkF8jNqwn64ti3VS8kVsv8TVC3LXzR/pddbGKUi0D0WQstORwsje6loo1uteqR/VapLJTIsC2SyGj8g0VT8mqdI5BJW9x4low63Pm9ZujfBcvSxqh4GajmpWzmBa1MJmz18Q6y9i5mwrEufEQ6JUs6nTlDvlb8Jt3BsBLubEa4S2i3ezc6pZ3nEthzetZkSa9mBfr4XclbUN17O7KPQLsutPb2HHRz9bGFvLOcxl38GOm3q+JP0yPy33aXTB1KqO90q18nlgx8e+VPxeLuAUyFL+rpayqjgHA+9xos1vXQoUsmly3O2/TWOo7zHdxxz8Dbx64LYePqQfKLPIXbMnBLHukWG88tD9el5STbkDnV2YNZuhnSZrs1nYHuXPX3DcrXbirDEmQo2baB08JiJEvNxi3RjrfN5ogle/DvB+LRAQjJXlC/h3px7D5G/tKBJbYl8vDePt5ItVt355hRuZjhgGstV0eazTvVKle2RDgSyUXBzGkJNv4l7+3T4v7Xbri/lLCznmQhQpqi+8VDoHA+9xok1vfVoovvQtIKWaM6PiIXFo7vu6WbIZ/adFHcbpF462Y3hfCkl7oFVw2RlEzqUwsi+DmTe8F4FsyrUsy3iwSrKGJAdoqWZh+3NCJMGoFe6ydukpTT8s20P0/dLGeR9fxhcavqGvtxlHgqjRr6Q/pJvg1fKZw9Pe8iCxfqrHG0MhY/YpN2ZlbE0jseTEljqW2X1SEFsuse3JBDDU7m6bi01jsrfUIGXTet0rlXnnI45zzkj/kRy+cP6/d1sbGzsGkYAzhkJ8TuSQOFdtS0ylc2jEocN6DIldiKh8jxPRxmqQP/XQ03Uhay3t59swXUUzJtGaiJry53a/hk9e/0P2n99h9v19+XiZ8ShEtF1xtCIRFVfQpbCI8aH1GuBJRFsdCxS0JZXuZqC6CXYFRWPAaf6z3URUXN27PIiIiGj7YQsFERERhcYCBREREYXGAgURERGFxgIFERERhcYCBREREYXGAgURERGFFupno5cuXdJTREREtJ3x36EgIiKi0NjlQURERKGxQEFEREShsUBBREREobFAQURERKGxQEFEREShsUBBREREobFAQURERKGxQEFEREShsUBBREREobFAEcLqVB+i8TRW9TzdHfzXdRGj0ShG5+2ZdbbOx5of9cXr4lgU0bFFPXdn2XkszlV+7kzero+NzMM1C8RBeXcy/teGz+HNgwUKorKa0Z/JoL9Fz95FmuMZZOLNeu5OWsWF87PoPi2Of5fm7d3j7o1/qr+6FygKS4uFJVyzdhKN9iG9rBfY64r5+TT6nOX2vtQ+CtZfluuNYlGWuJ3lRm3BPo6Yt2sRerlMh+/4gdpF6bRJ/nR8+2e39Pd0R5W67vb3zvURy/Xq0tqvayB+fccI7EunK20eq0LNyR+LM9iZzeol4sjB2q+9f+d4Ml3GsZzjmHlif3Q+iO8bDgwA411o198V7N+3rT+P5Lp9U2kjnyrVWleRjnvreseR6W5H1zjw9QMNRfPHzpMyz5DKaQkc29xXjbFjp0UsDz5DSiqVh/b3RWJSp02d06KRbrWtedy+KTOnKp9j0TgsEgfl1Zr3DpU+M83Fr6uThjLnY1PpcJebcRug8sy8T6rbjupA/s/B6mklHc9bvZP5FT2fzy/kRywrPzKn5gqWz43kLWtErCWpdb3let6K5yev21/kF5JiPqnWzl+fzJ8Qp+Ctv5Kf7PWWy2PJUzSPLefN7Z/DUXff1aQtntZLxbZHfcemO8a57sZ1jMl591qpOHCuVbjrqpb/3qJaFhfTTjw5x3HXDaYruO8AO11uOlRsm/Hqi3VJ7L8HPTpe9b1hLrfPy7tXCtaRy4188O1fLAM+5W1rzz/ru+8QvFeMtPv578NS814++hVcL30eZr6UTov/2ku+8wxeIzFfKXbkNTHj49OlrlHZPPSfg3Mc/zkF89s4rrx2az1HfWzfvnz5W04tee9nL3PToNLsW1emw15e4XwCaQiub8aLvZ17bsH9Fh6H6usOd3ksYnwISJzsRKP+Bi39SPVM4IxRku2OOcub0dYj/uo5js4m+ws0P90NLOXc0usN9Bj7a0RnTCw/O6NLvYAILhzTzXWNT7Xh83L9o7qZt+kQnu39MXLX5EyFtM3PYALdON6hlzZ14pvpuJqmO+6GuJLmdezotdA6eExEjNSIQ4dbMXv5qpiuz3W9TzZaiGVJX/OvOo7Jly4dvyodQarZ30uz7IJIQTw49Vx1up92thbEeWUySfdece+fikTtMDWBePplb1uxr4XkJQy/6tXorOQL7nJ5Lz2ZzSJntGK45scxfLEbKbc7RdyXJxN4ou9rvlaPMEqmRR4bCQw611OQ+dp99ow69r23a4gdRT5D3P2JGHgxaWHi9WBNt1Ieqmvhbrd8ATMij9qMrgQredLdVj7nxMvXi8uWNhGlubWdY9k4rF21cSCXtbrP4qvIifP9nc8NYMZp7Xhd3Hkyfiucz+rUGUz0pHz3nYwnDI27z/nsL38dV6f6EDsr4m7MuNd9xHZjGSSN41B93bECxa92iD+Wc3hr6Tvo2t3gNUGJT+ysWqeU1sf36KlCu6wDiDg3sPRoxA3w/yZf2Bb3YHB94Z17xR+V0nb1ZeBgBGZKGvdG9BTdebf1357IXv+DIrv6gXW6rl4z6sOdY/o7R2G6ipMP2GCa9yByUE+GYTTf7+/zulBKK5YWkZrH/YWloNslHh+rV3IFeYqmCA5Yj+iZ+pNpyd8H/OInbyF7Sjbne9c6Go2JQqOpcuz47Iv4XlB2vhiVGqVyHvoqQ9dymO1pcwuTRQXzULgd4hzXS6k4kNc84haCZjDwO0fwP+1tQe6KzIFFzIiXvyxQyXgpdz7LS2PI9u03lonPkWHM6uW27/8WYkPiG1+eqgrm7FC72qagG4Xq7Q63UIiCxXsdmLyetwdjmZ/NUGosl7bVW5/Qa9FWU7/r6hQkYsgNTtv7WNlMrVROQUI8bCN6wOOCqE1vJ/e/v2i3KEwb11l9dMvNzTv+yPPIVoaLM7ggXrB//icD/talGmzqc/SRLSOz+OqPxOTVAeBD+4B/+lX87DuvY1UU9HPGy7/c+dz8Bxas5EJgmfz0e9t/ZASpjGzViPnHdNitdmLdcwm0XhxWhRaOo1g3dyzyVJNxBJa1oLsY6uPd7Jy/uU2U/N+0LLsV4m8ajPbEMh65Kf6okDa71noxJ+ohHrsmRpuW1fiLul3XX8pWLNk9cjBhP/jCF4BVa4SqrTlULbeccjfs6hszotabsh+gtY3KL5YWkZrLvjpg1YrlqWwpmsu+o2fWRz4P7PjoZwuPHVagNcLOl0CrRXV5qF6w//4//zF++Ecjvu6Oaq3bOa4T2Sozf/kc/vh73Zg8LKJX3I8Hl36CH/0/30VEF6iKxouheItQgN2a04xjg62YOFFksKnursyc9neJU33VvUAhgyN76jW7FC7J/q8Bd+R6sQuuan1lR06XsRNn4fXzqn5Ms1+6ehXS1nIMiYPGWA9RG3y+oLmbNp86X1fzwTc/WqTLo1pOc6zXD7w4FjPuFf0gNR5+i68O4xUR8WUZD145qr66Lg+VlrHOL3pjHMS57e/7iNEPXwOdpzG3Jijuy5eG8XbyRbfvvZzyz5DS7rkh/ig4tlDkFxa1kM3x487zScTHUN9jRfKlujyUL9gz/+IZTFTq7ihhxzqd47p5NIJY/7/EV95SlTxV8JrAV7/y33kFqgrn09hxHN0XhzFkjLMr/MWI0tgxaOxL/XLE/KWJHLfh7xaheqp/C4U9EOltDB+RTcNRDOE4Jnu9ZtfGjqQ9IC4mm57sTww4vfbfOb+PL+MLDd/Q+2rH8L7UmmuP5dMmB/SkEHH6447k8BwHZW6YXdYuPVVZPa7r/bIVS8S2bz+pCFbmRkQhQzVjS7WkS+5vejDn7u/M4wnfoEz34aiXzzwtB20+oJcWsteHbtYVn/bLx1WXjFMosZvc5XL/T0JtIi35uUPufRs9kcPk9e+WLQCUPleZp9NILMXUvvR9WfW/eVHhGVKMlxZ1PWXTtzq2PBcgZTSP13SNpC99S+xA7+vIMA7Nfb94vlSTh+IayGu81u4OJeQ5BuKg1Mu5WmWPpQe9ei9xPZDZNz6k0vk0o/+cHISp71HxaT/fhumigy/Fvk4m0Gp3fahpc7vYUgLTG/Jvr2wPDfKnHnp66xG1hc/tfg2fvP6HVdV8iIhqIV+2pV9eayFbx2bQZrz8N56oyY9dwKF4vc6Rtqs7NoaCiGjbk+NwNluT+/w4Zh4/xMIEhbblCxQ1N18SEd1xqj/fbsrfbE3uLf2b4ld2tPVt7S4PIiIi2hTY5UFEREShsUBBREREobFAQURERKGxQEFEREShsUBBREREobFAQURERKGF+tnopUuX9BQRERFtZ/x3KIiIiCg0dnkQERFRaCxQEBERUWgsUBAREVFoLFAQERFRaCxQEBERUWgsUBAREVFoLFAQERFRaCxQEBERUWgsUBAREVFo27pAsTgWRXRsUc8RFbOI0WgUo/N6dgOsTvUhKtIgPxuZjrDs84insarn75Syx11Ooy/ah/Synq/F/Khvvxt1fnUXJk9oW2MLBdGmtooL52fRfTqDTCaD/hb9NdVHUyeSmSQ6m/Q82d7NvquniKpX9wJFYSndX8OTrQJ9U2n7u+K1rlWk494y377skvMoFmXNwFkuWxjs751txHK9up0WsdxuidDLy9bwzP2aJXT7e2+/0l1TG9mKdByk5TVwrlfZmmKxGFw04kxdazNO+qb8V3bnG//GXVZ43dX+3eVGq5dMixnvxeMvEPPu9nK/7egaB75+oKFovIW/3/Q+3OVmzVTuS8zPG/eXfSzzfL317f3cofutdJolf/q+/bNb+vsizNp4hbjyEWlsODAAjHeh3Uhr9tY1jBvXMhhH/nSb5+i/blLwnM18DeaPPy/9y9V1SftiLJguc99f+O5f40Hz1eB7vhZuS+SS/3OwelpJx/NW72R+Rc/n8wv5EcvKj8zpuaSVB47mJ6+reXt9a0SsZc/lJ3utfDxtbC3Wt5Jqaf76ZP6ESLI5H5PzJbaX+5an6O5PrP9pMW+mxd3X3IhY91NuutT8s3refw7Ocbx5uqOCcaCvj3ndK8egc22deSNOxLX3Ykpt682r9b39F48Nfwz+jhdXBdT63rkUny8Va+HutyLbFzv3wLlaVtyXd05a1bmWvt98xwpxv1WTZjMNR2Ws+PLIIJb3oCf/2t+I6b/5Qdm4KiCPa+zXOX833fY5Vcj7QLq9c/afZ/CcffP2+XvXxNlX8LqUSpc/nlVeAydKXIvCdBI5NqTLw0q+4DYxNj7VhiezWeRkDWF+HMNIYLCjUS0UmuMpdJ89o2oQ997GDXweiaPNamHTIXT0WmgdPAb1TSMOHW7F7OWr9pwkbhRvf02deDFpYeJ1X9leEDXE1ATi6Ze9ps+WfiwkL2H4VbluM9p64G23fAEzF7vRxubnDeOLA319zOteiZU86V7r5qe7IR7sOO7ESUsbupFTMal1n+7XMSbWP5rAE6e+hwti+erUGUz0pIyuiEZ0nkwAQ+NuDdHq/QwOlWpSlzEvYikVd/autn+i72uBWvfalbzfRArHh4DEyU5xVE3EfapnAmeMWmh3zFmu8hk9x315h6WcW4te//utQprnZzAhrp57LUUavpmOq+mK8uHjSpz/MScWRByNWD9G7pqckemWXVdeHDV2DCJx0J/X1WrsSCIzpvNAnH/G122jr5OhXLpmzprXWMVfj8iJ4prRz643KmFTjKG4LZKRvw/4xU/eQvaUbEL0mtei0Zh4QJhu6789kb3uo6XQvoj34BH2PN7qewAqV5G7WLgfe13N9+C8lsNsT5v7YKCNUBgHoRyMYI+eLNSKyKN6UmqK4ID1F/jLFWDlr8aQ7dtvxKv4HBnGrF61ktUrucJj2/t/RM/Un7zfbt8rJpZzeGvpO+ja3eBLf0y8YMppfbx0Tq37/VYpzVdfLsjPxr0RPVWNOseV8Ksd4g+R7mz2SX8ciZyK7NOTFTR2HEf3xWH9bAx28WhG18T+vqz+srSS6bLjb5eeacaxwVZMnNB5bXTnEQVtqkGZ97+/aJekp0UJWA5A8z669H1zA5Mra60XZ+xa6Z//yQC6n2ZxgoAPXZYtAAuBeJUfrya6mf3qvQ5MXs8XpD9ptBJuiDL3W7k0r976hF7rbqNaBjKZaSQOzmL4iHzB63ESTkFCFGQjevDuQtKyt6oHuzVEHvu0KOSdjdkFC46joGI2TYEinwd2fPSzwMWcqL/UUaB2dPWyqDsGalGiboTIQSB3JVCPkuu6ZDPiLP79f/5j/PCPRtjdsa3M6uZhTdTq5rK/iY8/LMq4/yxepAZePbv2HIx5e//v6Jn1cc9N8YeoiVrWgv/cwlrv+61Cmovlp90KtIHuk2NC7XS/GUj3KnJLerJqjegck4WGFLoxgZl58ez8D8cw25OyX/q1dEWUTJcdf0V+5WF3rWQwPdiK2fMX1hzzdPeqe4FC3tDZU6/ZNQtJ9jEPZCs3v90ju+xajtl9ijGzWa3IiO9ayC6UcWfktCjJD/U9ZvSROsRNGuvGWOcXvaZEcdz9fR/xrSubYc/8i2cwwe6OTW2tMVjORMoZbb+K9EvDeFuPS3CaooeMGltwdH5ZBTHv7P9Fo0+8tHDn6jRnl/+1QS3W/36rkGadn+64BJGG5zvH1PSGKkz36tSQPX5GjfdQhSxvvIkac+EoiCk9VkQWtP7m177gK8jJdavp8lB0ugLxfRY77bnCeFA/Y249fChQSCRajxYKe3DV27pJLoohHMdkb/nmt11uf50sfctBmKpZzf6cAFJG87G3bpW+9C2xA72vI8M4NPf94g9qke783CE33dETOUxe/65/XXswk8Xujk2gbBysIQbLa0XicE73X7fbA4en3UGUzeg/Jwdhtqu4EZ/2822YdgbMVSRjfhqJJSfmxf73idqmu/8KQt1vskCUtAc0xnTa5ZglnA4x6O4O3G/l06yeIRHnehzJ4bkKgzJlftgtNjfvqe35YnfLyHENJcY0BMh0Tw/m3HS3D0WMZ5tI98kEWt1n3wzaZBeDZg/gFJHnji8T+ZU4p7YNLmu/fBwr8pzPzhiFrtLs/NznbN+O3OEE4tYDeqmIb5EOdwyFjs8N7xKjTalB/tRDT991ZEm9tod7JbK0Lm70LdI/TnQn8X4j2t421aDMTU82M7K7g+jO4P1GtKWwQFGVVfWvzMnul2qboolojXi/EW1Fd3WXBxEREd0ZbKEgIiKi0FigICIiotBYoCAiIqLQWKAgIiKi0FigICIiotBYoCAiIqLQWKAgIiKikID/H8nR9Y5mK1WUAAAAAElFTkSuQmCC)

Metadata untuk tabel pertumbuhan ekonomi Amerika Serikat

Mencari tahu jenis tipe data menggunakan fungsi df.info()
"""

economics.info()

"""Terlihat dataset tersebut semua dalam tipe 'Object'. Cukup aneh. Jika diperhatikan baik-baik indeks kolom tidak dalam bentuk yang benar. Memperbaiki indeks kolom menggunakan fungsi dari Pandas."""

economics.set_axis(['date', 'pce', 'pop', 'psavert', 
                    'uempmed', 'unemploy'], axis='columns', inplace=True)
economics = economics.iloc[1: , :]

"""Cek ulang data"""

economics

"""Cek kembali jenis tipe data tersebut di setiap kolom."""

economics.info()

"""Jenis data yang kurang tepat dapat menyebabkan kesalahan dan menyulitkan dalam proses preprocessing data. Oleh karena itu, perlu setiap jenis data dirubah tipenya sesuai dengan hasil atau nilai yang ada.
Tipe data dapat diubah dengan menggunakan method astype yang tersedia pada library Pandas.
"""

economics['date'] = economics['date'].astype('datetime64')
economics['pce'] = economics['pce'].astype('float64')
economics['pop'] = economics['pop'].astype('float64')
economics['psavert'] = economics ['psavert'].astype('float64')
economics['uempmed'] = economics ['uempmed'].astype('float64')
economics['unemploy'] = economics ['unemploy'].astype('int64')

"""Mengubah index baris agar lebih enak dipandang menggunakan set_index method. Tambahkan argumen inplace='True' dengan tujuan agar perubahan tersebut diterapkan pada dataframe (override data)."""

economics.set_index('date', inplace=True)

"""Lakukan perhitungan analisis statistika sederhana menggunakan fungsi describe()"""

economics.describe()

"""Terlihat dari hasil, nilai terendah tidak menampilkan angka 0 sehingga tidak adanya data yang hilang.
Menampilkan dataframe economics kembali dengan tujuan melihat hasil akhir perubahan tersebut.
"""

economics

"""Salah satu hal yang perlu dilakukan sebelum melakukan pemodelan ialah dengan menghitung korelasi matriks dengan tujuan mengetahui korelasi variabel-variabel tersebut. Hal ini dapat dilakukan dengan menggunakan library matplotlib dan library seaborn."""

plt.figure(figsize=(10, 8))
correlation_matrix = economics.corr().round(2)
 
# Untuk menge-print nilai di dalam kotak, gunakan parameter anot=True
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, )
plt.title("Correlation Matrix untuk Fitur Numerik ", size=20)

"""Hasil matriks tersebut mendeskripsikan bahwa terdapat korelasi lemah antara variabel psavert dengan variabel target, yaitu ‘unemploy’ serta memiliki korelasi cukup tinggi dengan uempmed, pop dan pce (<0.5). Sehingga, dapat diabaikan.
Nilai-nilai numerik tersebut dapat dijabarkan dalam bentuk histogram agar membantu dalam pembacaan data.
"""

economics.hist(bins=50, figsize=(20,15))
plt.show()

"""Gunakan fungsi drop untuk menghapus kolom."""

economics.drop(['psavert'], inplace=True, axis=1)
economics.head()

"""Preprocessing kemudian dilakukan dengan tujuan agar pembuatan model machine learning dapat dilakukan dengan mudah dan tanpa hambatan. Preprocessing mencakup pembagian data test dan training (perbandingan 90:10, dengan nilai random state fixed tujuan agar memiliki value yang sama baik di bagian train maupun test."""

from sklearn.model_selection import train_test_split
 
X = economics.drop(["unemploy"],axis =1)
y = economics["unemploy"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 123)

"""Melakukan proses pengecekan dengan tujuan memastikan jumlah data yang terbagi."""

print(f'Total # of sample in whole dataset: {len(X)}')
print(f'Total # of sample in train dataset: {len(X_train)}')
print(f'Total # of sample in test dataset: {len(X_test)}')

"""Standarisasi perlu dilakukan agar menghindari kebocoran data selama proses training (pelatihan). Standarisasi dapat dilakukan dengan mudah dengan mengimpor fungsi StandardScaler. Lakukan terlebih dahulu untuk training data."""

from sklearn.preprocessing import StandardScaler
 
numerical_features = ['uempmed', 'pop']
scaler = StandardScaler()
scaler.fit(X_train[numerical_features])
X_train[numerical_features] = scaler.transform(X_train.loc[:, numerical_features])
X_train[numerical_features].head()

"""Melakukan pengecekan untuk memastikan standarisasi dilakukan dengan tepat."""

X_train[numerical_features].describe().round(4)

"""Mempersiapkan dataframe baru untuk proses pelatihan model-model yang akan digunakan, terdiri dari 'K-Nearest Neighborhood, Random Forest, Boosting Algorithm (Seperti yang dijelaskan dalam dokumen)"""

models = pd.DataFrame(index=['train_mse', 'test_mse'], 
                      columns=['KNN', 'RandomForest', 'Boosting'])

"""Perlu diketahui, dalam metode K-Nearest Neighborhood terdapat beberapa metriks yang dapat digunakan. Salah satunya ialah metrik euclidean yang digunakan untuk pembuatan model ini, dalam prosesnya model hanya menggunakan  k = 8 tetangga."""

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
 
knn = KNeighborsRegressor(n_neighbors=8)
knn.fit(X_train, y_train)
 
models.loc['train_mse','knn'] = mean_squared_error(y_pred = knn.predict(X_train), y_true=y_train)

"""Kemudian algoritma selanjutnya yang akan digunakan adalah algoritma random forest. Dalam prosesnya, Anda melakukan impor dengan bantuan sklearn library dengan menggunakan fungi RandomForestRegressor Anda dapat mengubah hyperparameter sesuai dengan yang Anda inginkan."""

# Impor library yang dibutuhkan
from sklearn.ensemble import RandomForestRegressor
 
# buat model prediksi
RF = RandomForestRegressor(n_estimators=50, max_depth=16, random_state=55, n_jobs=-1)
RF.fit(X_train, y_train)
 
models.loc['train_mse','RandomForest'] = mean_squared_error(y_pred=RF.predict(X_train), y_true=y_train)

"""Kemudian algoritma selanjutnya yang akan digunakan adalah algoritma boosting. Dalam prosesnya, Anda melakukan impor dengan bantuan sklearn library dengan method ensemble dengan membuat instantiate menggunakan fungi AdaBoostRegressor Anda dapat mengubah hyperparameter sesuai dengan yang Anda inginkan. Hyperprameter tersebut terdiri dari learning_rate serta random_state. """

from sklearn.ensemble import AdaBoostRegressor
 
boosting = AdaBoostRegressor(learning_rate=0.05, random_state=55)                             
boosting.fit(X_train, y_train)
models.loc['train_mse','Boosting'] = mean_squared_error(y_pred=boosting.predict(X_train), y_true=y_train)

"""Melakukan scaling terhadap fitur numerik pada X_test sehingga memiliki rata-rata=0 dan standar deviasi=1"""

X_test.loc[:, numerical_features] = scaler.transform(X_test[numerical_features])

"""Kemudian evaluasi model dilakukan dengan menggunakan algoritma mean squared error dengan membuat dataframe baru ditambahkan dengan kolom test dan train serta dictionary untuk setiap algoritma yang digunakan. Kemudian di akhir menghitung mse menggunakan for loop untuk train dan test data. Setelah itu, lakukan pemanggilan variabel mse."""

mse = pd.DataFrame(columns=['train', 'test'], index=['KNN','RF','Boosting'])
 

model_dict = {'KNN': knn, 'RF': RF, 'Boosting': boosting}
 

for name, model in model_dict.items():
    mse.loc[name, 'train'] = mean_squared_error(y_true=y_train, y_pred=model.predict(X_train))/1e3 
    mse.loc[name, 'test'] = mean_squared_error(y_true=y_test, y_pred=model.predict(X_test))/1e3
 

mse

"""Hasil performansi dari ketiga algoritma yang dipilih tersebut menunjukkan perbedaan yang cukup terlihat bagi model. Performansi menunjukkan bahwa algoritma random forest memiliki nilai mse yang lebih kecil dibandingkan dengan kedua model lainnya. Lakukan plotting terhadap performa menggunakan library matplotlib."""

fig, ax = plt.subplots()
mse.sort_values(by='test', ascending=False).plot(kind='barh', ax=ax, zorder=3)
ax.grid(zorder=0)

"""Lakukan perhitungan prediksi model untuk mengetahui tingkat akurasi dari prediksi yang dilakukan oleh model dengan hasil aktual."""

prediksi = X_test.iloc[:1].copy()
pred_dict = {'y_true':y_test[:1]}
for name, model in model_dict.items():
    pred_dict['prediksi_'+name] = model.predict(prediksi).round(1)
 
pd.DataFrame(pred_dict)

"""Hasil dari performa tersebut menunjukkan bahwa algoritma Random Forest menjadi algoritma paling sesuai untuk masalah tersebut. Setiap performa model tergantung dari kondisi permasalahan dan tentunya tersedianya data yang tentunya berbeda-beda, sehingga hal ini tergantung dari banyak kasus."""