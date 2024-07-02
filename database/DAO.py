from database.DB_connect import DBConnect


class DAO():

    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
        select distinct(Chromosome)
        from genes g 
        where Chromosome != 0
        """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row["Chromosome"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            select t1.c1, t1.c2, sum(t1.corr) as sumCorr
            from (select g1.Chromosome as c1, g2.Chromosome as c2, g1.GeneID as g1, g2.GeneID as g2, (i.Expression_Corr) as corr
                    from genes g1, genes g2, interactions i
                    where g1.GeneID = i.GeneID1 and g2.GeneID = i.GeneID2
                        and g1.Chromosome != g2.Chromosome and g1.Chromosome != 0 and g2.Chromosome != 0
                    group by g1.Chromosome, g2.Chromosome, g1.GeneID, g2.GeneID) as t1
            group by t1.c1, t1.c2
        """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append((row["c1"], row["c2"], row["sumCorr"]))

        cursor.close()
        conn.close()
        return result
