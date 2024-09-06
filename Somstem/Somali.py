# We put the main class here, where the rules are constructed.
#for future improvements, this is the main class you need to edit.
#for any confusion please contact Us.
class SomStemmermain:
    @staticmethod
    def do_som(word, suffixes, exceptions):
        Conn = ['b', 't', 'j', 'x', 'kh', 'd', 'r', 's', 'sh', 'dh', 'c', 'g', 'f', 'q', 'k', 'l', 'm', 'n', 'w', 'h','y']
        for suffix in suffixes:
            if word.endswith(suffix):
                return True
        return False
    @staticmethod
    def somstem(word):
        exceptions=[ 'oromo', 'axmaaro', 'tigree', 'lelkase', 'biciidyahan','tigre', 'uraago', 'jigjiga', 'arbe', 'maraykan','ciidan','wadan','ustareeliya', 'ustareliya','xildhibaan','garowe','wajaale','wajale','Caraaye','Xassan','soomaaliya','Kheyre','harboole','somaliland', 'bakayle', 'geelle','geele','helsinki','koow','gaarane','hawiya',
                    'ababa','mareexaan','bare', 'barre','cismaan', 'cusmaan','kenya','garoowe','abgaal','laasqoray', 'laasqorey','calmadow', 'Keeniya','kismaayo', 'kismayo','cadaado', 'cadado','gaalkacayo', 'galkacayo','maqale','shire','khaatumo','ssc-khaatumo','xassan','xassan',
                    'eriteriya','canada','cigaal','mareykan','maraykanka','sabriina','sabriin','saabriina','rayaale','hogaamiye','taliye','madaxweyne','onlf','muqdisho','shabeelay','ogaadeen', 'ogaden','ogadeen','galadiid', 'beercaano', 'dhooboweyn','lasdharkaynle', 'laasdharkaynle','dhanaan',
                     'caano','baydhaba','baydhabo','buula','qaylo ','afrikaan','gaadsan', 'ciidogale','shiine', 'ciise', "gare", "garre", "murursade", "murursadde", "sade","saleebaan", "xawaadle", "hawiye","daarood", "leelkase", "dhulbahante", "ciidagale", "habarjeclo", "muuse", "awrtable", "ortable", "majeerteen", "majerteen", "kaskiiqabe", "bartire", "yabaree", "yabarree", "wayteen", "weyteen", "jaarso", "gugundhabe", "raxanweyn", "raxanwayn", "cabdale", "baare", "shube", "isaayaas",
                     ]
              #We put these rules here for simplicity, it can be put inside the while loop.
        if word in exceptions:
                 return  word
        elif word.endswith('ceyn') :
             word = word.replace('ceyn', 'co')
             return word
        elif word.endswith('cayn'):
             word = word.replace('cayn', 'co')
             return word
        elif word.endswith('dorasho'):
             word = word.replace('dorasho', 'dorasho')
             return word
        elif word.endswith('laabtay'):
             word = word.replace('laabtay', 'laabasho')
             return word
        elif word.endswith(' amba-qaadayno'):
             word = word.replace('amba-qaadayno', 'amba-qaad')
             return word
        elif word.endswith('booqday'):
             word = word.replace('booqday', 'booqasho')
             return word
        elif word.endswith('gacmaha'):
             word = word.replace('gacmaha', 'gacmo')
             return word
        elif word.endswith('waalatey'):
             word = word.replace('waalatey', 'waalasho')
             return word
        elif word.endswith('Maareynta'):
             word = word.replace('Maareynta', 'Maaro')
             return word
        elif word.endswith('qadataa'):
             word = word.replace('qadataa', 'qadasho')
             return word
        elif word.endswith('waxbartay'):
            word = word.replace('waxbartay', 'waxbarasho')
            return word
        elif word.endswith('dhuuntay'):
            word = word.replace('dhuuntay', 'dhuumasho')
            return word
        elif word.endswith('burburin'):
            word = word.replace('burburin', 'burbur')
            return word
        elif word.endswith('soomaaliyeed'):
             word = word.replace('soomaaliyeed', 'soomaali')
             return word
        elif word.endswith('qaadayno'):
            word = word.replace('qaadayno', 'qaad')
            return word
        elif word.endswith('wadajirka'):
             word = word.replace('wadajirka', 'wadajir')
             return word
        elif word.endswith('dadaalada'):
             word = word.replace('dadaalada', 'dadaal')
             return word
        elif word.endswith('dadaallada'):
             word = word.replace('dadaallada', 'dadaal')
             return word
        elif word.endswith('cadalada'):
             word = word.replace('cadalada', 'cadalad')
             return word
        elif word.endswith('cadalaada'):
            word = word.replace('cadaalada', 'cadaalada')
            return word
        elif word.endswith('xariira'):
            word = word.replace('xariira', 'xariir')
            return word
        elif word.endswith('arrimaha'):
            word = word.replace('arrimaha', 'arrimo')
            return word
        elif word.endswith('arimaha'):
            word = word.replace('arimaha', 'arimo')
            return word
        elif word.endswith('xiriira'):
            word = word.replace('xiriira', 'xiriir')
            return word
        elif word.endswith('ceyna'):
             word = word.replace('ceyna', 'co')
             return word
        elif word.endswith('cayna'):
             word = word.replace('cayna', 'co')
             return  word
        elif word.endswith('jaaliyadda'):
             word = word.replace('jaaliyadda', 'jaaliyad')
             return  word
        elif word.endswith('madaxtooyada'):
             word = word.replace('madaxtooyada', 'madaxtooyo')
             return word
        elif word.endswith('dhaanto'):
            return word
        elif word.endswith('jeeda'):
            return word
        elif word.endswith('raysulwasaare'):
            return word
        elif word.endswith('leeyahay'):
            return word
        elif word.endswith('leeyihiin'):
            return word
        elif word.endswith('miisaaniyada'):
             return word
        elif word.endswith('shubay'):
             word = word.replace('ay', '')
             return  word
        elif word.endswith('ardayga'):
             word = word.replace('ardayga', 'arday')
             return word
        elif word.endswith('hadaba'):
             word = word.replace('hadaba', 'had')
             return  word
        elif word.endswith('nadaafada'):
             word = word.replace('nadaafada', 'nadaafo')
             return word
        elif word.endswith('jiida'):
             word = word.replace('jiida', 'jiid')
             return word
        elif word.endswith('dhawaaqa'):
             word = word.replace('dhawaaqa', 'dhawaaq')
             return word
        elif word == 'golaha':
            word = word.replace('golaha', 'gole')
            return word
        elif word.endswith('sheekadan'):
             word = word.replace('sheekadan', 'sheeko')
             return word
        elif word.endswith('wasaarada'):
             word = word.replace('wasaarada', 'wasaarad')
             return  word
        elif word.endswith('silsiladaha'):
             word = word.replace('silsiladaha', 'silsilad')
             return  word
        elif word.endswith('akhris'):
             word = word.replace('s', '')
             return  word
        elif word.endswith('biyo'):
             return  word
        elif word.endswith('jaajaale'):
            return word
        elif word.endswith('xiga'):
            return word
        elif word.endswith('xigga'):
            return word
        elif word.endswith('dagaal'):
            return  word
        elif word.endswith('laal'):
            return word
        elif word.endswith('dadaas'):
            word = word.replace('dadaas', 'do')
            return word
        elif word.endswith('naafadu'):
             word = word.replace('naafadu', 'naafo')
             return word
        elif word.endswith('xirfadaha'):
            word = word.replace('xirfadaha', 'xirfad')
            return word
        elif word.endswith('badani'):
            word = word.replace('badani', 'badan')
            return word
        elif word == 'guryaha':
            word = word.replace('guryaha', 'guryo')
            return word
        elif word.endswith('maqnaa'):
            word = word.replace('maqnaa', 'maqan')
            return word
        elif word.endswith('hadla'):
            word = word.replace('hadla', 'hadal')
            return word
        elif word.endswith('aashii'):
            word = word.replace('aashii', 'aal')
            return word
        elif word.endswith('aashu'):
            word = word.replace('aashu', 'aal')
            return word
        elif word.endswith('aashan'):
            word = word.replace('aashan', 'aal')
            return word
        elif word == 'noqonayaa':
            word = word.replace('noqonayaa', 'noqosho')
            return word
        elif word == 'mashquulsan':
            word = word.replace('mashquulsan', 'mashquul')
            return word
        elif word.endswith('aasha'):
            word = word.replace('aasha', 'aal')
            return word
        elif word.endswith('madow'):
            return word
        elif word.endswith('maxay'):
            return word
        elif word.endswith('madoow'):
            return word
        elif word.endswith('wada'):
            return word
        elif word.endswith('tolow'):
              return word
        elif word.endswith('maanta'):
            return word
        elif word.endswith('waxayse'):
             return word
        elif word.endswith('ilkacase'):
              return word
        elif word.endswith('ladhahaa'):
              return word
        elif word.endswith('malaayiin'):
              return word
        elif word.endswith('walow'):
              return word
        elif word.endswith('allah'):
              return word
        elif word.endswith('aakhir'):
              return word
        elif word.endswith('akhir'):
              return word
        elif word.endswith('akhar'):
             return word
        elif word.endswith('aakhar'):
             return word
        elif word.endswith('sarkaal'):
              return word
        elif word.endswith('madaxweyne'):
            return word
        elif word.endswith('madaxwayne'):
            return word
        suffixes = [
                    'yaashaan','yaashii','jireen','jirteen','jirnay','jiray','jirin','jirney','jirnay','jirteen','sanahay','sanahey','soco',
                     'hooda', 'heena', 'hayga', 'hiina', 'asheena','shooda','shiina','shaada','gooda','gaaga', 'gayga', 'aashaa','aasha','aashay','ashay',
                     'hooda', 'heena', 'hayga', 'hiina', 'asheena','shooda','shiina','shaada','gooda','gaaga', 'gayga','yeeli','aashood','aashayda','ashayda','aashiin','ashiin',
                    'iin','karnaa','kartaan','maayaan','maysaan','heena','kareen','hiisa','kartaa','maysid','jirtay','yiin','sadeen','koodii','sanayn','mayaa','yahan','meey','sheen','shiin','shay',
                    'nahay','yahay','yahow','yoow','mayso','mayno','karo','kara','karaa','maayo','badan','tahay','tiiye','taasi','nimadu','sanaan','nimada','nimadda',
                    'itaan','ow','tooyo','sanaa','keenu','keen','heed','hood','heen','keed','kaas','kaan','kiina','saan','yaan','ayaan','yan','yeen','yen','taan','taann','taanno','nimo',
                   'bay', 'ay','ahay','daro','na','yay','tay','tey','nay','ey','san','yaal','nina','nin','no','seen','leey','doo',
                    'kan','kaa','kii','ki','kuu','ku','kee','dee','ke','gee','ga','ka','aal','aay','she','oow','oob','baa','ba','sii','tan',
                    'tid','sid','id','niin','to','gu','gii','no','ta','tu','tii','da','du','so','iyiin',
                    'dii','taa','sa','na','naa','eey','eed','kood','jir','le','leh','la','to','do','aad','sha','dha','das','yaa',
                    'taa','saa','tee','koow','yey','say','teen','een','seen','ya','yihiin','sa','ah','oo','ayaa','aa','ka','ee','tee','yaabo','eenu','iinu','iisu','yaro','aysay',
                    'kaasi','haasi','hiisa','uu','gooda','kasta','keede', 'dhaw', 'dooda ','kiisi',
                 #lo,#yo, an,'aan',aal? nimadisa, nimadooda, nimadeeda, nimadeena, nimadiina kood day ,'kay' iyiin
                 #'weyn',nno, nna
        ]
        #Our main Body.
        while True:
            matched_suffix = None
            for suffix in suffixes:
                if word.endswith(suffix):
                    matched_suffix = suffix
                    #the above rules in exception can be placed here also, the algorihtm works same.
                elif word == 'magaala':
                    word = word.replace('magaala', 'magaalo')
                    return word
                elif word == 'walaash':
                    word = word.replace('walaash', 'walal')
                    return word
                elif word == 'adigaa':
                    word = word.replace('adigaa', 'adiga')
                    return word
                elif word == 'leedahay':
                    word = word.replace('leedahay', 'leedahay')
                    return word
                elif word == 'umada':
                    word = word.replace('umada', 'umad')
                    return word
                elif word == 'dulqaadanayay':
                    word = word.replace('dulqaadanayay', 'dulqaad')
                    return word
                elif word == 'waawayn':
                    word = word.replace('waawayn', 'waawayn')
                    return word
                elif word == 'bilaawday':
                    word = word.replace('bilaawday', 'bilaaw')
                    return word
                elif word == 'lkn':
                    word = word.replace('lkn', 'laakiin')
                    return word
                elif word == 'jawaabo':
                    word = word.replace('jawaabo', 'jawaab')
                    return word
                elif word == 'qoritaan':
                    word = word.replace('qoritaan', 'qor')
                    return word
                elif word == 'birlab':
                    word = word.replace('birlab', 'bir')
                    return word
                elif word == 'biyole':
                    word = word.replace('biyole', 'biyo')
                    return word
                elif word == 'baadhitaan':
                    word = word.replace('baadhitaan', 'baadh')
                    return word
                elif word == 'dilan':
                    word = word.replace('dilan', 'dil')
                    return word
                elif word == 'karsi':
                    word = word.replace('karsi', 'kar')
                    return word
                elif word == 'cagaaran':
                    word = word.replace('cagaaran', 'cagaar')
                    return word
                elif word == 'guduudan':
                    word = word.replace('guduudan', 'guduud')
                    return word
                elif word == 'fariidah':
                    word = word.replace('fariidah', 'fariid')
                    return word
                elif word == 'baduugan':
                    word = word.replace('baduugan', 'baduug')
                    return word
                elif word == 'jawaabaan':
                    word = word.replace('jawaabaan', 'jawaab')
                    return word
                elif word == 'siyaasada':
                    word = word.replace('siyaasada', 'siyaasad')
                    return word
                elif word == 'wadatay':
                    word = word.replace('wadatay', 'wadasho')
                    return word
                elif word == 'mashruciini':
                    word = word.replace('mashruciini', 'mashruc')
                    return word
                elif word == 'aragtidaada':
                    word = word.replace('aragtidaada', 'aragti')
                    return word
                elif word == 'shuruudii':
                    word = word.replace('shuruudii', 'shuruud')
                    return word
                elif word == 'matalaad':
                    word = word.replace('matalaad', 'matalaad')
                    return word
                elif word == 'noqotay':
                    word = word.replace('noqotay', 'noqosho')
                    return word
                elif word == 'qaateen':
                    word = word.replace('qaateen', 'qaadasho')
                    return word
                elif word == 'macangaga':
                    word = word.replace('macangaga', 'macangag')
                    return word
                elif word == 'Beelaha':
                    word = word.replace('Beelaha', 'Beel')
                    return word
                elif word == 'puntland':
                    word = word.replace('puntland', 'puntland')
                    return word
                elif word == 'maamuladii':
                    word = word.replace('maamuladii', 'maamul')
                    return word
                elif word == 'iyadu':
                    word = word.replace('iyadu', 'iyadu')
                    return word
                elif word == 'hambalyo':
                    word = word.replace('hambalyo', 'Hambalyo')
                    return word
                elif word == 'dhuunto':
                    word = word.replace('dhuunto', 'dhuumasho')
                    return word
                elif word == 'illaa':
                    word = word.replace('illaa', 'illaa')
                    return word
                elif word == 'guulihii':
                    word = word.replace('guulihii', 'guul')
                    return word
                elif word == 'saaka':
                    word = word.replace('saaka', 'saaka')
                    return word
                elif word == 'hooyeen':
                    word = word.replace('hooyeen', 'hooyeen')
                    return word
                elif word == 'guulaha':
                    word = word.replace('guulaha', 'guul')
                    return word
                elif word == 'ammaanay':
                    word = word.replace('ammaanay', 'ammaan')
                    return word
                elif word == 'jubbaland':
                    word = word.replace('jubbaland', 'jubbaland')
                    return word
                elif word == 'kusoo':
                    word = word.replace('kusoo', 'kusoo')
                    return word
                elif word == 'xeryo':
                    word = word.replace('xeryo', 'xeryo')
                    return word
                elif word == 'qaado':
                    word = word.replace('qaado', 'qaado')
                    return word
                elif word == 'qabto':
                    word = word.replace('qabto', 'qabasho')
                    return word
                elif word == 'annaga':
                    word = word.replace('annaga', 'annaga')
                    return word
                elif word == 'bilowday':
                    word = word.replace('bilowday', 'bilow')
                    return word
                elif word == 'qabanayo':
                    word = word.replace('qabanayo', 'qabasho')
                    return word
                elif word == 'loogu':
                    word = word.replace('loogu', 'loogu')
                    return word
                elif word == 'keenaan':
                    word = word.replace('keenaan', 'keenid')
                    return word
                elif word == 'keenan':
                    word = word.replace('keenan', 'keenid')
                    return word
                elif word == 'mooto':
                    word = word.replace('mooto', 'mooto')
                    return word
                elif word == 'maraysay':
                    word = word.replace('maraysay', 'marid')
                    return word
                elif word == 'qaraxu':
                    word = word.replace('qaraxu', 'qarax')
                    return word
                elif word == 'hooyo':
                    word = word.replace('hooyo', 'hooyo')
                    return word
                elif word == 'kamid':
                    word = word.replace('kamid', 'kamid')
                    return word
                elif word == 'federaal':
                    word = word.replace('federaal', 'federaal')
                    return word
                elif word == 'itoobiya':
                    word = word.replace('itoobiya', 'itoobiya')
                    return word
                elif word == 'tirsan':
                    word = word.replace('tirsan', 'tiro')
                    return word
                elif word == 'gudaha':
                    word = word.replace('gudaha', 'gudo')
                    return word
                elif word == 'sixid':
                    word = word.replace('sixid', 'sixid')
                    return word
                elif word == 'noqonaya':
                    word = word.replace('noqonaya', 'noqosho')
                    return word
                elif word == 'kale':
                    word = word.replace('kale', 'kale')
                    return word
                elif word == 'sanno':
                    word = word.replace('sanno', 'sanno')
                    return word
                elif word == 'dhuumanayay':
                    word = word.replace('dhuumanayay', 'dhuumasho')
                    return word
                elif word == 'goojacade':
                    word = word.replace('goojacade', 'goojacade')
                    return word
                elif word == 'booqanaya':
                    word = word.replace('booqanaya', 'booqasho')
                    return word
                elif word == 'ergey':
                    word = word.replace('ergey', 'ergey')
                    return word
                elif word == 'afrika':
                    word = word.replace('afrika', 'afrika')
                    return word
                elif word == 'yimid':
                    word = word.replace('yimid', 'yimid')
                    return word
                elif word == 'badbaaday':
                    word = word.replace('badbaaday', 'badbaadid')
                    return word
                elif word == 'jiritaan':
                    word = word.replace('jiritaan', 'jiritaan')
                    return word
                elif word == 'adkaaday':
                    word = word.replace('adkaaday', 'adkaasho')
                    return word
                elif word == 'xulufadii':
                    word = word.replace('xulufadii', 'xulufu')
                    return word
                elif word == 'lasoo':
                    word = word.replace('lasoo', 'lasoo')
                    return word
                elif word == 'qalalaase':
                    word = word.replace('qalalaase', 'qalalaase')
                    return word
                elif word == 'khudbadii':
                    word = word.replace('khudbadii', 'khudbad')
                    return word
                elif word == 'waligay':
                    word = word.replace('waligay', 'waligay')
                    return word
                elif word == 'labaad':
                    word = word.replace('labaad', 'labo')
                    return word
                elif word == 'k𝙤𝙤𝙬':
                    word = word.replace('k𝙤𝙤𝙬', 'k𝙤𝙤𝙬')
                    return word
                elif word == 'l𝙖𝙗𝙤':
                    word = word.replace('l𝙖𝙗𝙤', 'l𝙖𝙗𝙤')
                    return word
                elif word == 's𝙖𝙙𝙙𝙚𝙭':
                    word = word.replace('s𝙖𝙙𝙙𝙚𝙭', 's𝙖𝙙𝙙𝙚𝙭')
                    return word
                elif word == 'iyaga':
                    word = word.replace('iyaga', 'iyaga')
                    return word
                elif word == 'banaan':
                    word = word.replace('banaan', 'banaan')
                    return word
                elif word == 'gaysatay':
                    word = word.replace('gaysatay', 'gaysi')
                    return word
                elif word == ' laba-geeriyaad':
                    word = word.replace(' laba-geeriyaad', ' laba-geeriyood')
                    return word
                elif word == 'maskiinta':
                    word = word.replace('maskiinta', 'maskiinta')
                    return word
                elif word == 'qalatay':
                    word = word.replace('qalatay', 'qalasho')
                    return word
                elif word == 'cafinaayo':
                    word = word.replace('cafinaayo', 'cafis')
                    return word
                elif word == 'mooryaana':
                    word = word.replace('mooryaana', 'mooryaan')
                    return word
                elif word == 'danbaysay':
                    word = word.replace('danbaysay', 'danbayn')
                    return word
                elif word == 'dareen':
                    word = word.replace('dareen', 'dareen')
                    return word
                elif word == 'balse':
                    word = word.replace('balse', 'balse')
                    return word
                elif word == 'maantoy':
                    word = word.replace('maantoy', 'maanta')
                    return word
                elif word == 'madaxwaynahiina':
                    word = word.replace('madaxwaynahiina', 'madaxwayne')
                    return word
                elif word == 'mase':
                    word = word.replace('mase', 'mase')
                    return word
                elif word == 'geysateen':
                    word = word.replace('geysateen', 'geysi')
                    return word
                elif word == 'gaysateen':
                    word = word.replace('gaysateen', 'gaysi')
                    return word
                elif word == 'fanaan':
                    word = word.replace('fanaan', 'fanaan')
                    return word
                elif word == 'geeriyooday':
                    word = word.replace('geeriyooday', 'geeri')
                    return word
                elif word == 'isaga':
                    word = word.replace('isaga', 'isaga')
                    return word
                elif word == 'taqaano':
                    word = word.replace('taqaano', 'taqaan')
                    return word
                elif word == 'siyaasadiisa':
                    word = word.replace('siyaasadiisa', 'siyaasad')
                    return word
                elif word == 'indhahayga':
                    word = word.replace('indhahayga', 'indho')
                    return word
                elif word == 'wacdiyaa':
                    word = word.replace('wacdiyaa', 'wacdi')
                    return word
                elif word == 'mise':
                    word = word.replace('mise', 'mise')
                    return word
                elif word == 'damiirkaada':
                    word = word.replace('damiirkaada', 'damiir')
                    return word
                elif word == 'hortaada':
                    word = word.replace('hortaada', 'horta')
                    return word
                elif word == 'xildhibaanimo':
                    word = word.replace('xildhibaanimo', 'xildhibaan')
                    return word
                elif word == 'xadaya':
                    word = word.replace('xadaya', 'xadaya')
                    return word
                elif word == 'hoose':
                    word = word.replace('hoose', 'hoos')
                    return word
                elif word == 'fatwoonaya':
                    word = word.replace('fatwoonaya', 'fatwo')
                    return word
                elif word == 'shalay':
                    word = word.replace('shalay', 'shalay')
                    return word
                elif word == 'dhiiga':
                    word = word.replace('dhiiga', 'dhiig')
                    return word
                elif word == 'xamsena':
                    word = word.replace('xamsena', 'xamse')
                    return word
                elif word == 'xasuusatid':
                    word = word.replace('xasuusatid', 'xasuus')
                    return word
                elif word == 'xilkaahayay':
                    word = word.replace('xilkaahayay', 'xil')
                    return word
                elif word == 'moodaa':
                    word = word.replace('moodaa', 'mood')
                    return word
                elif word == 'samata':
                    word = word.replace('samata', 'sama')
                    return word
                elif word == 'alle':
                    word = word.replace('alle', 'alle')
                    return word
                elif word == 'ilaahay':
                    word = word.replace('ilaahay', 'ilaahay')
                    return word
                elif word == 'eegatay':
                    word = word.replace('eegatay', 'eeg')
                    return word
                elif word == 'meeldhexaad':
                    word = word.replace('meeldhexaad', 'meel')
                    return word
                elif word == 'careysan':
                    word = word.replace('careysan', 'caro')
                    return word
                elif word == 'faxsharan':
                    word = word.replace('faxsharan', 'faxshar')
                    return word
                elif word == 'barnaamijyada':
                    word = word.replace('barnaamijyada', 'barnaamij')
                    return word
                elif word == 'gobolada':
                    word = word.replace('gobolada', 'gobol')
                    return word
                elif word == 'doraadto':
                    word = word.replace('doraadto', 'doraad')
                    return word
                elif word == 'kayar':
                    word = word.replace('kayar', 'yar')
                    return word
                elif word == 'kaweyn':
                    word = word.replace('kaweyn', 'weyn')
                    return word
                elif word == 'kawayn':
                    word = word.replace('kawayn', 'wayn')
                    return word
                elif word == 'kafiican':
                    word = word.replace('kafiican', 'fiican')
                    return word

                    break
                elif word.endswith('keyn'):
                    word = word.replace('keyn', 'ko')
                elif word.endswith('kayn'):
                    word = word.replace('kayn', 'ko')
                elif word.endswith('keyna'):
                    word = word.replace('keyna', 'ko')
                elif word.endswith('kayna'):
                    word = word.replace('kayna', 'ko')
                    return word
                elif word.endswith('raduhu'):
                    word = word.replace('raduhu', 'rad')
                    return word
                elif word.endswith('midnimadda'):
                    word = word.replace('midnimadda', 'midnimo')
                    return word
                elif word.endswith('laha'):
                     word = word.replace('laha', '')
                     return word
                elif word.endswith('radaha'):
                    word=word.replace('radaha', 'rad')
                    return  word
                elif word=='sam':
                    word = word.replace('sam', 'samayn')
                    return word
                elif word=='miyaa':
                    word = word.replace('miyaa', 'miyaa')
                    return word
                elif word == 'ganacsa':
                     word = word.replace('ganacsa', 'ganacso')
                     return word
                elif word == 'faa':
                     word = word.replace('faa', 'faan')
                     return word
                elif word == 'lum':
                    word = word.replace('lum', 'lumid')
                    return word
                elif word == 'Qaybihii':
                    word = word.replace('Qaybihii', 'Qayb')
                    return word
                elif word == 'yaraatee':
                     word = word.replace('yaraatee', 'yar')
                     return word
                elif word == 'badn':
                     word = word.replace('badn', 'badni')
                     return word
                elif word == 'gabagab':
                     word = word.replace('gabagab', 'gabagabo')
                     return word
                elif word == 'gabageb':
                    word = word.replace('gabageb', 'gabagebo')
                    return word
                elif word == 'abgaal':
                     return word
                elif word == 'inaan':
                     return word
                elif word.endswith('diyaaradu'):
                     word=word.replace('diyaaradu', 'diyaarad')
                     return word
                elif word.endswith('sanayo'):
                    word = word.replace('sanayo', '')
                    return word
                elif word == 'same':
                    word = word.replace('same', 'samayn')
                    return word
                elif word=='bilow':
                    return word
                elif word=='dibjir':
                    return word
                elif word == 'liitay':
                     word = word.replace('liitay', 'liidmo')
                     return word
                elif word == 'qeybgash':
                    word = word.replace('qeybgash', 'qeybgal')
                    return word
                elif word == 'habeen':
                    return word
                elif word == 'dambee':
                     word = word.replace('dambee', 'dambe')
                     return word
                elif word == 'dambe':
                     return word
                elif word == 'danbee':
                    word = word.replace('danbee', 'danbe')
                    return word
                elif word == 'danbe':
                    return word
                elif word == 'badana':
                     word = word.replace('badana', 'badan')
                     return word
                elif word.endswith('lamay') and len(word) > 3:
                    word = word.replace('lamay', '')
                elif word.endswith('geli') and len(word) > 4:
                    word = word.replace('geli', '')
                elif word == 'warar':
                      word = word.replace('warar', 'war')
                      return word
                elif word == 'niman':
                      word = word.replace('niman', 'nin')
                      return word
                elif word == 'doona':
                     return word
                elif word.endswith('duqeyn'):
                    return word
                elif word == 'dawlada':
                     word = word.replace('dawlada', 'dawlad')
                     return word
                elif word == 'xarumihii':
                     word = word.replace('xarumihii', 'xarun')
                     return word
                elif word == 'xarumaha':
                    word = word.replace('xarumaha', 'xarun')
                    return word
                elif word == 'qoomiyadaha':
                    word = word.replace('qoomiyadaha', 'qoomiyad')
                    return word
                elif word == 'khasaare':
                    return word
                elif word == 'shaqaaqo':
                    return word
                elif word == 'sheekay':
                     word = word.replace('sheekay', 'sheeko')
                     return word
                elif word == 'dhexe':
                    word = word.replace('dhexe', 'dhex')
                    return word
                elif word == 'liitey':
                     word = word.replace('liitey', 'liidmo')
                     return word
                elif word == 'badnaa':
                    word = word.replace('badnaa', 'badan')
                    return word
                elif word == 'gidig':
                    word = word.replace('gidig', 'gidi')
                    return word
                elif word == 'akhar':
                    word = word.replace('akhar', 'aakharo')
                    return word
                elif word == 'akhir':
                    word = word.replace('akhir', 'aakharo')
                    return word
                elif word == 'aakhir':
                    word = word.replace('aakhir', 'aakharo')
                    return word
                elif word == 'aakhar':
                    word = word.replace('aakhar', 'aakharo')
                    return word
                elif word == 'kaalayd':
                     word = word.replace('kaalayd', 'kaalay')
                     return word
                elif word == 'kaala':
                    word = word.replace('kaala', 'kaalay')
                    return word
                elif word == 'kaal':
                    word = word.replace('kaal', 'kaalay')
                    return word
                elif word == 'jaamacaduhu':
                    word = word.replace('jaamacaduhu', 'jaamacad')
                    return word
                elif word == 'guryuhu':
                    word = word.replace('guryuhu', 'guri')
                    return word
                elif word == 'guryo':
                    word = word.replace('guryo', 'guri')
                    return word

                elif word == 'wejah':
                     word = word.replace('wejah', 'wejahid')
                     return word
                elif word == 'wajah':
                     word = word.replace('wajah', 'wajahid')
                     return word

                elif word == 'beeral':
                     word = word.replace('beeral', 'beeraley')
                     return word

                elif word == 'gacm':
                    word = word.replace('gacm', 'gacmo')
                    return word

                elif word == 'fagaar':
                     word = word.replace('fagaar', 'fagaare')
                     return word

                elif word == 'beeraha':
                     word = word.replace('beeraha', 'beer')
                     return word
                elif word.endswith('ada'):
                     word = word.replace('ada', 'o')
                     return word

                elif word == 'beeerahii':
                     word = word.replace('beeerahii', 'beer')
                     return word
                elif word == 'shaqeyn':
                     word = word.replace('shaqeyn', 'shaqo')
                     return word
                elif word == 'shaqa':
                     word = word.replace('shaqa', 'shaqo')
                     return word
                elif word == 'xeryah':
                    word = word.replace('xeryah', 'xero')
                    return word
                elif word == 'xerad':
                    word = word.replace('xerad', 'xero')
                    return word

                elif word == 'haween':
                     return word
                elif word == 'xumo':
                     return word
                elif word == 'sheekha':
                     word = word.replace('sheekha', 'sheekh')
                     return word
                elif word == 'sheekh':
                     return word
                elif word == 'sheekhu':
                    word = word.replace('sheekhu', 'sheekh')
                    return word
                elif word == 'katirsan':
                     return word
                elif word == 'gabadha':
                     return word
                elif word == 'dusha':
                    return word
                elif word == 'tihiin':
                    return word
                elif word == 'biy':
                    word = word.replace('biy', 'biyo')
                    return word
                elif word == 'xiga':
                    word = word.replace('xiga', 'xigasho')
                    return word
                elif word == 'biyoh':
                    word = word.replace('biyoh', 'biyo')
                    return word
                elif word == 'biya':
                    word = word.replace('biya', 'biyo')
                    return word
                elif word == 'biyaha':
                    word = word.replace('biyaha', 'biyo')
                    return word
                elif word == 'gabdha':
                    word = word.replace('gabdha', 'gabadh')
                    return word
                elif word == 'dhacday':
                    word = word.replace('dhacday', 'dhacdho')
                    return word
                elif word == 'tareen':
                    return word
                elif word == 'taren':
                    return word
                elif word == 'weey':
                    word = word.replace('weey', 'weeydin')
                    return word
                elif word == 'mareykan':
                     return word
                elif word == 'xooga':
                    word = word.replace('xooga', 'xoog')
                    return word
                elif word == 'gabdh':
                    word = word.replace('gabdh', 'gabadh')
                    return word
                elif word == 'dhasheen':
                    word = word.replace('dhasheen', 'dhalasho')
                    return word
                elif word == 'kuliyada':
                    word = word.replace('kuliyada', 'kuliyad')
                    return word
                elif word == 'kulliyada':
                    word = word.replace('kulliyada', 'kulliyad')
                    return word
                elif word == 'mareegaha':
                     word = word.replace('mareegaha', 'mareeg')
                     return word
                elif word == 'jabha':
                    word = word.replace('jabha', 'jabhad')
                    return word
                elif word == 'taliyayaal':
                    word = word.replace('taliyayaal', 'taliye')
                    return word
                elif word == 'shisheeye':
                    return word
                elif word == 'kuxigeen':
                      return word
                elif word == 'ciyaaraha':
                    word = word.replace('ciyaaraha', 'ciyaar')
                elif word == 'ciyaaruhu':
                    word = word.replace('ciyaaruhu', 'ciyaar')
                elif word == 'ciyaarihii':
                    word = word.replace('ciyaarihii', 'ciyaar')
                elif word == 'ciyaarahii':
                    word = word.replace('ciyaarahii', 'ciyaar')
                elif word.endswith('hadla'):
                    word = word.replace('hadla', 'hadal')
                    return word
                elif word.endswith('telefiishanka'):
                    word = word.replace('telefiishanka', 'telefiishan')
                    return word
                elif word.endswith('gaal'):
                    word = word.replace('keyn', 'ko')
                elif word.endswith('kayn'):
                    word = word.replace('kayn', 'ko')
                elif word.endswith('keyna'):
                    word = word.replace('keyna', 'ko')
                elif word.endswith('kayna'):
                    word = word.replace('kayna', 'ko')
                elif word.endswith('ra'):
                    word = word.replace('a', 'o')
                elif word.endswith('abbaaraha'):
                    word = word.replace('abbaaraha', 'abbaar')
                elif word.endswith('eeka'):
                    word = word.replace('eeka', 'eeko')
                elif word.endswith('raja'):
                    word = word.replace('raja', 'rajo')
                elif word.endswith('aala'):
                    word = word.replace('aala', 'aal')
                elif word.endswith('shada'):
                    word = word.replace('shada', 'sho')
                elif word.endswith('uraha'):
                    word = word.replace('uraha', 'uro')
                elif word.endswith('bilaaba'):
                    word = word.replace('bilaaba', 'bilaaw')
                elif word.endswith('daa'):
                    word = word.replace('daa', 'daal')
                elif word.endswith('dibada'):
                    word = word.replace('dibada', 'dibad')
                    return word
                elif word.endswith('dooda'):
                    word = word.replace('dooda', 'dood')
                    return word
                elif word.endswith('hadl'):
                    word = word.replace('hadl', 'hadal')
                    return word
                elif word=='dhima':
                    word = word.replace('dhima', 'dhimasho')
                    return word
                elif word == 'heesaha':
                    word = word.replace('heesaha', 'hees')
                    return word
                elif word == 'masuuliyad':
                    word = word.replace('masuuliyad', 'masuul')
                    return word
                elif word == 'maaliyad':
                    word = word.replace('maaliyad', 'maal')
                    return word
                elif word == 'hambal':
                    word = word.replace('hambal', 'hambalyo')
                    return word
                elif word == 'hambaly':
                    word = word.replace('hambaly', 'hambalyo')
                    return word
                elif word.endswith('xalay'):
                    return word
                elif word.endswith('arday'):
                    return word
                elif word.endswith('laakiin'):
                    return word
                elif word.endswith('laakin'):
                    return word
                elif word.endswith('lakin'):
                    return word
                elif word.endswith('dhaliila'):
                    word = word.replace('dhaliila', 'dhaliil')
                    return word

                elif word.endswith('lahayn'):
                     return word
                elif word.endswith('doonaan'):
                    word = word.replace('doonaan', 'doona')
                    return word
                elif word.endswith('donaan'):
                    word = word.replace('donaan', 'doona')
                    return word
                elif word.endswith('doonan'):
                    word = word.replace('doonan', 'doona')
                    return word
                elif word.endswith('jecl'):
                    word = word.replace('jecl', 'jecel')
                    return word
                elif word.endswith('gobola'):
                    word = word.replace('gobola', 'gobol')
                    return word
                elif word == 'filanayo':
                    word = word.replace('filanayo', 'filasho')
                    return word
                elif word=='dhin':
                    word = word.replace('dhin', 'dhimasho')
                    return word
                elif word == 'qabsa':
                    word = word.replace('qabsa', 'qabsasho')
                    return word
                elif word == 'fadhid':
                    word = word.replace('fadhid', 'fadhi')
                    return word
                elif word == 'soc':
                    word = word.replace('soc', 'socod')
                    return word
                elif word == 'weyn' or word=='wayn':
                     return word
                elif word=='beesha' :
                    return word
                elif word == 'ciyaal':
                     return word
                elif word == 'duleed':
                     return word
                elif word == 'kasoo':
                     return word
                elif word == 'iyadoo':
                    return word
                elif word == 'iyado':
                    return word
                elif word == 'iyadiiy':
                    word = word.replace('iyadiiy', 'iyada')
                    return word
                elif word == 'laaba':
                    word = word.replace('laaba', 'laabasho')
                    return word
            if matched_suffix:
                if len(word[:-len(matched_suffix)]) <3:
                    break
                word = word[:-len(matched_suffix)]
            else:
                break
        consonants = 'bcdfghjklmnpqrstvwxy' # Somali Alphabets
        if word.endswith('mayn') and len(word) > 3:
            word = word.replace('ayn', 'ee')
        elif word.endswith('hore') and len(word) > 3:
                word = word.replace('hore', '')
        elif word.endswith('asho') and word[-3] == 'r' and len(word) > 3:
            word = word.replace('asho', 'ro')
        elif word.endswith('asho') and len(word) > 3:
            word = word.replace('asho', 'o')
        elif word.endswith('asha') and len(word) > 3:
            word = word.replace('asha', 'o')
        elif word.endswith('shan') and len(word) > 3:
            word = word.replace('shan', 'l')
        elif word.endswith('yo') and word[-2] != 'o' and len(word) > 3:
            word = word.replace('yo', ' ')
        elif word.endswith('iye') and len(word) > 3 and word[0] !='h':
             word = word.replace('iye', 'i')
        elif word.endswith('jin') and len(word) > 3:
             word = word.replace('jin', 'ji')
        elif word.endswith('limiin') and len(word) > 3:
             word = word.replace('limiin', 'lin')
        elif word.endswith('ooy') and len(word) > 3:
             word = word.replace('ooy', 'o')
        elif word.endswith('mo') and len(word) > 3:
            word = word.replace('mo', 'in')
        elif word.endswith('ooyin') and len(word) > 3:
             word = word.replace('ooyin', 'o')
        elif word.endswith('badan') and len(word) > 3:
            word = word.replace('badan', ' ')
        elif word.endswith('baddan') and len(word) > 3:
            word = word.replace('baddan', ' ')
        elif word.endswith('iyad') and len(word) > 3:
             word = word.replace('iyad', 'i')
        elif word.endswith('kaba') and len(word) > 3:
            word = word.replace('kaba', '')

        elif word.endswith('ayn') and len(word) > 4 and word !='falanqayn':
            word = word.replace('ayn', '')
        elif word.endswith('bax') and len(word) > 4 and word !='anbabax':
            word = word.replace('bax', '')
        elif word.endswith('adani') and len(word) > 3 and word[-6] != 'q' and word[-6] != 'c':
            word = word.replace('adani', 'o')
        elif word.endswith('adani') and len(word) > 3 and word[-6]== 'q' and word[-6] == 'c' and word[-7] == 'i':
            word = word.replace('adani', 'ad')
        elif word.endswith('eyn') and len(word) > 3:
            word = word.replace('eyn', '')
        elif word.endswith('dhuhu') and len(word) > 3:
             word = word.replace('dhuhu', 'dho')
        elif word.endswith('lashii') and len(word) > 3:
             word = word.replace('lashii', 'lal')
        elif word.endswith('uhu') and len(word) > 3:
             word = word.replace('uhu', 'e')
        elif word.endswith('xaha') and len(word) > 3:
             word = word.replace('aha', '')
        elif word.endswith('aha') and len(word) > 3 and word!='heesaha' and word[-4] !='d' and word[-4] !='l' and word[-4] !='b':
             word = word.replace('aha', 'e')
        elif word.endswith('baha') and len(word) > 3:
             word = word.replace('aha', ' ')
        elif word.endswith('laha') and len(word) > 3:
             word = word.replace('aha', ' ')
        elif word.endswith('daha') and len(word) > 3:
             word = word.replace('aha', '')
        elif word.endswith('ihii') and len(word) > 3:
            word = word.replace('ihii', 'e')  #why o
        elif word.endswith('ihi') and len(word) > 3:
            word = word.replace('ihi', 'o')
        elif word.endswith('ha') and len(word) > 3:
             word = word.replace('ha', '')
        elif word.endswith('naan') and len(word) > 3 and word[-5] !='o':
            word = word.replace('naan', 'an')
        elif word.endswith('sl') and len(word) > 3:
            word = word.replace('sl', 'sal')
        elif word.endswith('qo') and len(word) > 3:
            word = word.replace('qo', 'q')
        elif word.endswith('rk') and len(word) > 3:
            word = word.replace('rk', 'rka')
        elif word.endswith('ood') and len(word) > 3 and word[-4] !='r':
            word = word.replace('ood', 'o')
        elif word.endswith('lkay') and len(word) > 3:
            word = word.replace('lkay', 'lko')
        elif word.endswith('ashadan') and len(word) > 3:
            word = word.replace('ashadan', 'o')
        elif word.endswith('aago') and len(word) > 3:
            word = word.replace('aago', 'aag')
        elif word.endswith('ado') and len(word) > 3:
            word = word.replace('ado', 'ad')
        elif word.endswith('laashay') and len(word) > 3:
            word = word.replace('laashay', 'laal')
        elif word.endswith('lashay') and len(word) > 3:
            word = word.replace('lashay', 'lal')
        elif word.endswith('laashey') and len(word) > 3:
            word = word.replace('laashey', 'laal')
        elif word.endswith('lashey') and len(word) > 3:
            word = word.replace('lashey', 'lal')
        elif word.endswith('wal') and len(word) ==3:
            word = word.replace('wal', 'walal')
        elif word.endswith('socd') and len(word) > 3:
            word = word.replace('socd', 'socod')
        elif word.endswith('daas') and len(word) > 3:
            word = word.replace('daas', 'd')
        elif word.endswith('kani') and len(word) > 3:
            word = word.replace('kani', '')
        elif word.endswith('dhint') and len(word) > 3:
            word = word.replace('dhint', 'dhimasho')
        elif word.endswith('an') and word[-3] !='d' and len(word[-3]) > 3:
             word = word.replace('an', '')
        elif word == 'ark':
            word = word.replace('ark', 'arag')
            return word
        elif word == 'falanq':
            word = word.replace('falanq', 'falanqayn')
            return word
        elif word == 'labad':
            word = word.replace('labad', 'labo')
            return word
        elif word == 'daawad':
            word = word.replace('daawad', 'daawasho')
            return word
        elif word == 'jaw':
            word = word.replace('jaw', ' jawaab')
            return word
        elif word == 'isag':
             word = word.replace('isag', 'isaga')
             return word
        elif word == 'daawat':
            word = word.replace('daawat', 'daawasho')
            return word
        elif word == 'shaqa':
            word = word.replace('shaqa', 'shaqo')
            return word
        elif word == 'dag':
             word = word.replace('dag', 'dagaal')
             return word

        elif word == 'ansixiy':
            word = word.replace('ansixiy', 'ansixi')
            return word
        elif word == 'maleshi':
            word = word.replace('maleshi', 'maleshiyo')
            return word
        elif word == 'dhegays':
            word = word.replace('dhegays', 'dhegaysi')
            return word
        elif word == 'cambaar':
            word = word.replace('cambaar', 'cambaarayn')
            return word
        elif word == 'sayg':
            word = word.replace('sayg', 'say')
            return word

        elif word == 'dhuf':
            word = word.replace('dhuf', 'dhufasho')
            return word
        elif word == 'aab':
            word = word.replace('aab', 'aabo')
            return word
        elif word == 'qarama':
            word = word.replace('qarama', 'qaramo')
            return word
        elif word == 'maleeshi':
            word = word.replace('maleeshi', 'maleshiyo')
            return word
        elif word == 'maql':
             word = word.replace('maql', 'maqal')
             return word
        elif word == 'wat':
            word = word.replace('wat', 'wadasho')
            return word
        elif word == 'wadat':
            word = word.replace('wadat', 'wadasho')
            return word
        elif word == 'dagma':
             word = word.replace('dagma', 'dagmo')
             return word
        elif word == 'ciidama':
             word = word.replace('ciidama', 'ciidan')
             return word
        elif word == 'baadhi':
             word = word.replace('baadhi', 'baadhid')
             return word
        elif word == 'shaq':
             word = word.replace('shaq', 'shaqo')
             return word
        elif word == 'jeedi':
             word = word.replace('jeedi', 'jeedin')
             return word
        elif word == 'xadi':
             word = word.replace('xadi', 'xadidid')
             return word
        elif word == 'hanjab':
             word = word.replace('hanjab', 'hanjabid')
             return word
        elif word.endswith('hadash'):
            word = word.replace('hadash', 'hadal')
            return word
        elif word.endswith('a') and len(word[-1]) > 3:
             word = word.replace('a', '')
        elif word.endswith('e') and len(word) > 3 and word[-2] != 'b'  and word[0] !='h':
             word = word.replace('e', '')
        #elif word.endswith('a'):
             #word = word.replace('a', '')
        if len(word) > 2 and word[-1] in consonants and word[-2] in consonants and word[-1] != 'h' and word[-2] !='y' and word[-2] != 'w':
              word = word[:-1]
        prefix = ['ja', 'fud', 'waa', 'yar', 'cus','dhaa','ad','gu',] #currently identified prefixes in Somali.
        for pre in prefix:
                if word.startswith(pre + pre[0]):
                    word = word[len(pre):]
                    break
        return word

# The end of the rules.

