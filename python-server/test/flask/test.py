from keyword_service import KeywordService
# from theme_service import ThemeService
from openai_service import OpenAIService
import openai_service
keyword_service = KeywordService()
# theme_service = ThemeService()
# openai_service = OpenAIService()


texts = []
texts.append("""불구속 수사를 받게 된 박정훈 전 해병대 수사단장이 오늘(5일) 오전 국방부 검찰단에 출석했습니다. 박 전 단장의 법률 대리인은 출석 전 기자들과 만나 이번 사건은 국방부 장관에서 해병대 수사단장에 이르기까지 명령이 하달됐는지 밝혀야 하는 사건이라며 진술 거부권을 행사하지 않고 조사에 응할 예정이라고 밝혔습니다. 이어 군 검찰 수사심의위원회 소집 요청이 받아들여지지 않은 것과 관련해서는 법적 의무 사항이 아니지만 회피한다는 생각이 든다고 말했습니다. 박 전 단장 측은 또 해병 순직 사건에 대한 보강 수사를 하고 싶다고 밝힌 의미에 대해 범죄 사실이 명확하지 않게 민간 경찰에 이첩됐다며 국방부 조사본부의 재검토 결과는 부족하다고 생각한다고 설명했습니다. 앞서 국방부 검찰단은 박 전 단장에게 항명과 상관 명예훼손 혐의를 적용해 구속영장을 청구했지만, 중앙지역군사법원은 현 단계에서 증거인멸이나 도망의 염려 등을 인정하기 어렵다며 기각했습니다. ※ '당신의 제보가 뉴스가 됩니다' [카카오톡] YTN 검색해 채널 추가 [전화] 02-398-8585 [메일] social@ytn.co.kr""")
texts.append("""객차 안으로 빗물이 쏟아져 들어옵니다. 스페인의 수도 마드리드 등 스페인 중부지역에 하루 만에 92mm의 큰비가 쏟아지며 지하철이 침수되고, 버스 수십 대가 흙탕물에 잠겼습니다. 1981년 이후 40여 년 만에 가장 많은 비로 마드리드 지역 다리 6개가 무너지고 도로 곳곳이 폐쇄됐습니다. [크리스티나 도밍고 : 마드리드 근교 주민: 비가 너무 많이 와서 집이 무너질까봐 걱정했는데 다리가 끊겨서 모든 사람이 정말 깜짝 놀랐어요. 이런 일이 벌어지리라고는 솔직히 생각 못했거든요] 전역에서 사망자가 속출했고 강에서, 진흙 속에서 실종자를 찾는 작업도 계속됐습니다. 톨레도에서는 헬리콥터까지 동원해 지붕에 피신한 사람들을 구조했습니다. [마드리드 근교 주민 : 자고 있었는데, 비가 많이 와서 무섭다는 이웃 전화를 받았어요. 등 뒤에서 쓰레기통 쳐대는 듯한 소리가 들리더니 집 안으로 파도처럼 물이 밀려 들어왔어요.] 마드리드와 톨레도를 잇는 철도는 일부 구간이 침수돼 열차 운행이 중단됐고 프리메라리가 축구 경기도 취소됐습니다. 스페인에선 지난달까지 40도를 오르내리는 폭염과 가뭄이 계속됐는데 폭우 피해까지 겹친 겁니다. 전문가들은 기후 변화로 지중해 상공 공기가 더워지면서 이런 극한 현상이 발생하고 있다고 분석했습니다. YTN 기정훈입니다. 영상편집:안윤선 화면제공:Lorena Ontiveros,Manuel ;Torres, @dtorresmayoral 자막뉴스:이선 #YTN자막뉴스 #스페인폭우""")
texts.append("""차세대소형위성 2호, 폭우 쏟아진 7월 16일 촬영 국내는 물론 미국·남극 등 전 세계 곳곳 포착 영상레이다, 날씨·시간 관계없이 영상 촬영 가능[앵커] 지난 5월 누리호에 실려 우주로 날아간 차세대소형위성 2호가 초기 운영을 성공적으로 마치고, 관측 영상을 공개했습니다. 순수 국내 기술로 개발한 영상레이다가 날씨와 관계없이 전 세계 곳곳을 촬영하는 데 성공했습니다. 양훼영 기자입니다. [기자] 제주도 한라산 국립공원의 백록담과 제주도 전역에 있는 오름이 선명하게 보입니다. 누리호가 싣고 간 차세대소형위성 2호에 탑재된 영상레이다가 촬영한 것으로, 장마철 2배에 육박하는 폭우가 쏟아졌던 지난 7월 16일에 찍은 사진입니다. 간조 시각에 갯벌이 드러난 목포시 일대와 설악산 국립공원은 물론 미국 나이아가라 폭포, 통가 화산섬, 북극과 남극 등 전 세계 곳곳도 생생히 포착했습니다. 가시광선이 아닌 마이크로파로 촬영한 건데, 영상레이다는 신호처리를 통해 영상을 만들어 날씨나 시간과 관계없이 지상관측이 가능하기 때문입니다. 특히, 순수 우리 기술로 개발한 영상레이다를 통해 처음 지구를 촬영했다는 점에서 의미가 큽니다. [장태성 / KAIST 인공위성연구소 단장 : 차세대소형위성 2호는 위성 본체와 탑재체 대부분이 국내 독자 기술로 개발되었으며, 이러한 귀중한 기술 자산을 통해서 영상레이다 기술을 확보하는 데 도움됐습니다.] 차세대소형위성 2호에는 국산화한 핵심 탑재체 4종을 포함해 6개의 탑재체가 실려있는데, 모두 정상 작동한다는 사실을 지난 석 달 동안 확인했습니다. KAIST 인공위성연구소는 탑재체 기술검증 임무를 8개월 동안 추가 진행한 뒤 북극의 해빙 변화와 산림 변화 탐지 등을 위한 정보 수집에 들어갈 예정입니다. YTN 사이언스 양훼영입니다. ※ '당신의 제보가 뉴스가 됩니다' [카카오톡] YTN 검색해 채널 추가 [전화] 02-398-8585 [메일] social@ytn.co.kr""")
texts.append("""상해 폭행 건이 888건에 달하고 또 툭하면 자는 아이 깨우거나 싸움 말리는 부분도 다 아동학대로 신고되고 있기 때문에 선생님들이 직접적인 교실 질서 유지하는 데 어려움이 있는 것은 여전히 존재하고 있습니다. [앵커] 지금 말씀하신 그 아동학대와 관련된 부분이 많은 선생님들이 말씀하시는 핵심적인 내용 중의 하나일 것 같은데요. 그래서 지금 일단 교육부 고시는 시행이 됐고 법으로 바꿔야 되는 부분들, 이른바 4법에 대해서 입법이 진행되고 있지 않습니까? [김동석] 그렇습니다. [앵커] 그 4법의 개정안에 대해서는 어떻게 생각하십니까? [김동석] 일단은 가장 중요한 핵심적인 교권 입법이라고 보고 있고요. 툭하면 아동학대 신고되는 부분을 막기 위해서 정상적인 교육 활동이나 생활지도는 아동학대로 보지 아니한다는 초중등 교육법은 조속히 국회 본회의를 통과하여야 합니다. 두 번째로는 지금 교권 침해 가해 학생들에 대한 즉시 가분리 조치 부분이 어렵기 때문에 그런 부분들도 보완이 돼야 될 부분이고, 이번에 아직 입법이 되고 있지 않은 교권침해 가해 학부모에 대한 처벌 조항이 현실적으로 없거든요. 이런 부분도 마련이 돼야 되고, 특히 유치원에서도 교권침해나 아동학대 문제가 심각하기 때문에 유아교육법 개정안, 또 학부모의 의무를 강조하는 교육기본법 개정안, 이 교육 4법이 조속히 교육 위원회 전체회의와 본회의 통과를 촉구합니다. [앵커] 그러니까 7일에 어쨌건 여, 야, 정부, 그다음에 시도 교육감들은 이 내용에는 합의를 했고 7일에 국회 교육위원회 법안심사소위원회를 통과할 예정으로 알려져 있고 이르면 21일, 이번 달 21일에 국회 본회의를 통과한다라는 것이 지금 시간표인데요. 지금 말씀하신 가해 학부모 처벌에 대해서는 이 4법에는 포함돼 있지 않은 것이고요? [김동석] 그렇습니다. 실제적으로 지금 현재 교권 침해를 하는 학부모에 대해서는 사과 권고나 화해 권고 말고 할 수 있는 게 없거든요. 실제로 학교에서 악성 민원이나 교권 침해 부분에 가해 학부모가 점점 늘고 있는데 실질적인 제재 조치 마련을 촉구하고 있습니다. [앵커] 그다음에 아까 말씀하신 유아교육에서 그 문제는 유아교육법 개정안, 이 4법 중 하나 개정안에는 포함이 안 돼 있습니까? [김동석] 포함이 되어 있고요. 유치원 교원에 대한 생활지도권을 부여하고 유치원 교육도 정상적인 교육활동이나 생활지도는 아동학대로 보지 않아야 한다는 조항은 포함이 돼서 환영을 합니다. 조속히 본회의 통과를 촉구합니다. [앵커] 아까 저희보여드린 내용 중에 교권침해하는 학생의 학생생활기록부에 기재하는 내용, 이 내용이 지금 쟁점인 것 같은데 야당에서 이 부분은 이게 소송의 남발로 갈 수 있고 학생한테 낙인이 될 수 있고 반대한다고 하는데, 거기에 대해서는 어떤 입장이십니까? [김동석] 지금 현재 법안심사에서 통과된 것이 학교교권보호위원회를 지역 교육청으로 이관한다고 합의가 돼서 전체적으로 통과될 것으로 보여집니다. 따라서 야당에서 주장하시는 학교가 소송의 장이 될 것이라는 부분은 지역 교육청으로 이관하게 되면 자연이 해소될 것이고요. 특히 말씀드렸듯이 교사를 폭행하고 상해하려는 그런 심각한 교권 침해를 하는 학생들에 대한 학급 교체, 강제 전학, 퇴학 조치는 경종을 울리기 위해서라도 학생부에 기재하여야 한다, 이렇게 저희들은 주장하고 있습니다. [앵커] 학급을 옮기거나 퇴학하는 것 그 조치는 하더라도 학생기록부에까지 남기는 것은 과하다라는 지적에 대해서는 어떻게 보시는지요? [김동석] 학생부의 목적이 학생의 건전한 활동 부분이나 또 교육 부분을 보여주는 모습이거든요. 지금 현재 금주에 발표한 대학입시요강에도 학교폭력 사안에 대해서는 기록을 하고 또 제재를 가하도록 그렇게 바뀌었지 않습니까? 자기 스승에 대한, 선생님에 대한 폭행이라든지 중대한 교권 침해에 대해서 학생부 기재를 통해서 경각심을 줘야 된다는 것이 많은 선생님들의 요구이고, 저희들의 3만 2951명의 설문조사나 또 국민여론을 보더라도 학생부 기재의 필요성은 상당 부분 공감을 하고 있습니다. [앵커] 알겠습니다. 그래서 지금 원안대로 교권회복 4법은 조속히 국회에서 통과돼야 된다라는 입장이십니다. 그런데 현장 교사들께서는 이 4법이 통과되더라도 아동학대법이 같이 바뀌지 않으면 이게 실효성이 없을 것이다라고 하시는 분들도 있다는데 어떤 얘기입니까? [김동석] 지금 아동학대처벌법에 아동학대 신고한 자에게는 어떠한 불이익한 처분을 하여서는 아니된다는 조항이 있습니다. 결국에는 비록 나중에 가서 경찰, 검찰에서 무혐의가 된다 하더라도 기소율 자체는 실제로 아동학대 신고돼도 교사가 1.4%밖에 안 되거든요. 결국에는 모든 교사들이 아동학대까지 가지 않은 행동임에도 무고성 무분별한 아동학대 신고가 많은데 결국은 무고성 아동학대 신고자에 대한 처벌조항이 없다면 이러한 악순환은 계속되지 않을 것이냐 하는 우려이고요. 아동학대처벌법 개정을 통해서 이런 교사 보호를 위한 후속적인 법률 개정 부분이 반드시 뒤따라야 된다는 것이 현장 교사들의 요구입니다. [앵커] 그런데 지금 교권회복 4법에 교원의 정당한 생활지도는 아동학대 금지행위 위반이 아니다라는 것이 명시가 되어 있지 않습니까? [김동석] 네, 비록 돼 있다 하더라도 학부모가 무고성 아동학대 남발 부분 자체를 막을 수는 없거든요. 결국에는 경찰, 검찰 조사, 특히 아동학대처벌법상 비록 검경수사권 조정으로 경찰 단계가 중요하게 되었지만 검찰 수사까지 무조건 받아야 된다는 심리적 압박과 부담 부분은 여전히 존재할 수 있는 개연성을 걱정하고 있는 것입니다. [앵커] 그러니까 정당한 생활지도이냐를 판정받기까지 교원들, 교사들께서 고통을 받을 수밖에 없다라는 말씀이신 거죠? [김동석] 그렇습니다. [앵커] 이게 최근에 계속해서 비극적인 사건들 저희가 소식을 접하고 있는데요. 제주교총을 지내셨던 교사께서도 그렇고 또 서울 양천구, 그다음에 용인에서 잇따라 이런 안타까운 극단적인 선택을 하신 선생님들 소식 들려오고 있습니다. 그 상황을 좀 파악하고 계십니까? [김동석] 그렇습니다. 어제 49재가 열리는 날에도 전 제주회장님께서 안타까운 소식이 들렸고 또 서울, 경기, 전북에 이어서 계속해서 이런 슬픈 소식이 들려오다 오니까 전국의 선생님들이 소식 또 뉴스가 들릴 때마다 비통한 부분을 많이 전해오고 있습니다. 이제는 이런 비극과 슬픔이 없도록 우리 스스로의 노력도 필요하지만 교육 입법과 또 국민들의 적극적인 응원과 격려가 필요하지 않을까 싶습니다. [앵커] 알겠습니다. 김동석 한국교총 교권본부장께 듣고 있습니다. 일각에서는 교권이 회복되는 것이 자칫하면 학생 인권이 약화되는 것과 연결되는 것이 아니냐 우려하시는 분도 있거든요? [김동석] 우리 선생님들의 교권은 말씀드렸듯이 학생의 교육을 위해서 의미가 있다고 생각을 합니다. 교권이 올라간다고 해도 과거처럼 과거회귀적으로 우리 학생들의 인권을 탄압을 하거나 또 인권을 저해하는 요소 부분은 결코 있을 수 없다고 생각합니다. 말씀드렸듯이 많은 학생들은 학교에서 95% 되는 학생들이 학교에서 인권을 존중받고 있다고 생각하거든요. 학생의 인권을 존중하면서 또 교사의 교권을 존중받는 인권 친화적인 학교를 만드는 것이 교사들의 바람이고 이런 안전한 학교에서 성장한 아이들이 민주시민으로 성장하지 않겠습니까? 우리 학생들 존중하고 사랑하면서 우리 선생님들도 자긍심과 열정으로 우리 아이들을 열심히 공부시키고 싶은 그런 간절한 마음을 호소드리고 싶습니다. [앵커] 알겠습니다. 선생님들이 계속 거리로 오고 계시고 지난 주말에도 수십만 명이 모였다고 하는데 질서가 굉장히 아주 모범적으로 지켜졌고 법을 준수했고 역시 선생님들다웠다, 그런 평가들을 들었습니다. 그때 현장에 계셨습니까? [김동석] 그렇습니다. 매번 선생님의 외침을 보고 또 끝날 때까지 다 정리를 하고 나올 때의 그 마음은 진짜 선생님들답다. 한 건의 사건사고도 없고 깨끗하게 청소하고 나가시는 모습을 보면서 이것이 바로 가장 교육적인 집회의 모습이 아닐까. 또 우리 아이들에게 보여주고, 또 국민들이 이런 모습을 보면서 응원해 주시지 않을까 그런 생각을 늘 갖고 집에 돌아오곤 했습니다. [앵커] 알겠습니다. 여야정 그리고 시도 교육감까지 4자가 합의한 교권회복 4법. 조속히 입법되기를 많은 국민들이 바라고 있고요. 지금 지적하신 현장에서 그래도 미흡한 부분 그런 부분들도 꼼꼼하게 잘 정부가 챙겨서 해결되도록 했으면 좋겠습니다. 한국교총 김동석 교권복지본부장님 고맙습니다. [김동석] 감사합니다. ※ '당신의 제보가 뉴스가 됩니다' [카카오톡] YTN 검색해 채널 추가 [전화] 02-398-8585 [메일] social@ytn.co.kr""")

keywords = keyword_service.get_keywords(texts)
print(keywords)

print("결과물은?")
# themes_of_keywords = openai_service.get_themes_of_keywords(list(keywords.keys()))
# print(themes_of_keywords)


print(openai_service.make_prompt(list(keywords.keys())))