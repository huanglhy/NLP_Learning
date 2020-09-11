1.下载最新中文维基百科数据集  https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2
2.wikiextractor解压，提取数据集中正文信息  wiki 
python WikiExtractor.py -b 1000M -o wiki_00 zhwiki-latest-pages-articles.xml.bz2 
3.利用opencc将提取到的中文信息 wiki转换为简体（win10环境下，cmd执行）
opencc -i D:\pycharm_project\knowledge_rule\datas\wiki\AA\wiki_00 -o D:\pycharm_project\knowledge_rule\datas\wiki\AA\wiki_00_j.txt -c D:\job_soft\opencc-1.0.4-win32\opencc-1.0.4\share\opencc\t2s.json
4.预处理（去掉<doc>、\n等；分词、去停用词）
5.训练word2vec模型
6.将模型作为工具进行相似度计算等。
7.导入知识，将知识向量化并将问题和答案分别存储到json文件
8.测试