# -*- coding: utf-8 -*-

import MySQLdb
import MySQLdb.cursors
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class MyprojectPipeline(object):
    def process_item(self, item, spider):
        conn = MySQLdb.connect(host='localhost',
                               port=3306,
                               user='root',
                               passwd='yms',
                               db='yuanmingsong',
                               charset='utf8')
        cur = conn.cursor()
        cur.execute('insert into data(Url, Title, the_text) VALUES(%s,%s,%s)',
                     (item['myurl'], item['mytitle'], item['mytext']))
        conn.commit()
        cur.close()
        conn.close()
        f = open(item['title'], 'w')
        data = item['myurl']+'\n'+item['mytitle']+'\n'+item['mytext']+'\n'
        f.write(data)
        f.close()
        return item


















# import MySQLdb
# import MySQLdb.cursors
# import sys
#
#
#
# class MyprojectPipeline(object):
#      def process_item(self, item, spider):
#             reload(sys)
#             sys.setdefaultencoding('utf-8')
#             conn = MySQLdb.connect(host='localhost',
#                                    port=3306,
#                                    user='root',
#                                    passwd='yms',
#                                    db='yuanmingsong',
#                                    charset='utf8')
#             cur = conn.cursor()
#             cur.execute('insert into data(Url, Title, the_text) VALUES(%s,%s,%s)', (item['myurl'], "item['mytitle']", "item['mydata']"))
#             conn.commit()
#             cur.close()
#             conn.close()
#             return item


            #self.dbpool = adbapi.ConnectionPool('MySQLdb',**dbargs)
            #res = self.dbpool.runInteraction(self.updata, item)

    # def updata(self, conn, item):
     #    conn.execute('insert into data(Url, Title, Text) VALUES(%s,%s,%s)',(item['myurl'],"item['mytitle]","item['mytext]"))
