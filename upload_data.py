import requests
import consts
r = requests.post(consts.URL_ENREGISTREMENT, json={"type":"temperature","donnees":[[21,1584972536],[21,1584972539],[21,1584972542],[21,1584972854],[21,1584972874],[21,1584972884],[21,1584972923],[21,1584972931],[21,1584972963],[21,1584972973],[21,1584972981],[21,1584972983],[22,1584975676],[21,1584975679],[21,1584975681],[21,1584975683],[21,1584975686],[21,1584975688],[21,1584975691],[21,1584975698],[21,1584975700],[21,1584975703],[21,1584975705],[21,1584975707],[21,1584975710],[21,1584975712],[21,1584975714],[21,1584975717],[21,1584975719],[20,1584976358],[19,1584976361],[19,1584976364],[19,1584976366],[19,1584976368],[20,1584976371],[20,1584976373],[20,1584976376],[20,1584976383],[20,1584976385],[20,1584976388],[20,1584976390],[20,1584976392],[21,1584976397],[20,1584976398],[19,1584976399],[20,1584976400],[20,1584976401],[20,1584976402],[20,1584976403],[20,1584976403],[20,1584976404],[20,1584976405],[19,1584976406],[19,1584976407],[22,1584976414],[20,1584976415],[20,1584976415],[19,1584976416],[20,1584976417],[20,1584976417],[19,1584976423],[19,1584976429],[19,1584976429],[19,1584976430],[19,1584976435],[19,1584976436],[20,1584976436],[20,1584976442],[19,1584976442],[20,1584976443],[19,1584976444],[20,1584976444],[19,1584976445],[20,1584976445],[20,1584976456],[20,1584976457],[19,1584976457],[20,1584976458],[20,1584976458],[21,1584976963],[21,1584977059],[21,1584977127],[21,1584977186],[21,1584977189],[21,1584977191],[21,1584977194],[21,1584977197],[21,1584977199],[21,1584977212],[21,1584977215],[21,1584977217],[21,1584977220],[21,1584977222],[21,1584977225],[21,1584977227],[21,1584977230],[21,1584977233],[21,1584977235],[21,1584977238],[21,1584977240],[21,1584977243],[21,1584977245],[21,1584977248],[21,1584977250],[21,1584977253],[21,1584977256],[21,1584977258],[21,1584977261],[21,1584977263],[21,1584977266],[21,1584977269],[21,1584977271],[21,1584977274],[21,1584977276],[21,1584977279],[21,1584977282],[21,1584977284],[21,1584977286],[21,1584977289],[21,1584977292],[21,1584977294],[21,1584977297],[21,1584977299],[21,1584977302],[21,1584977304],[21,1584977307],[21,1584977310],[21,1584977312],[21,1584977315],[21,1584977657],[21,1584977660],[21,1584977667],[21,1584977683],[21,1584977685],[21,1584977688],[21,1584977690],[21,1584977693],[21,1584977696],[21,1584977698],[21,1584977703],[21,1584977711],[21,1584977713],[21,1584977718],[21,1584977721],[21,1584977729],[21,1584977731],[21,1584977734],[21,1584977749],[21,1584977751],[21,1584977754],[21,1584977756],[21,1584977759],[21,1584977762],[21,1584977764],[21,1584977767],[21,1584977774],[21,1584977777],[21,1584977779],[21,1584977782],[21,1584977784],[21,1584977787],[21,1584977790],[21,1584977792],[21,1584977796],[21,1584977798],[21,1584977801],[21,1584977804],[21,1584977806],[21,1584977809],[21,1584977811],[21,1584977814],[21,1584977816],[21,1584977819],[21,1584977822],[21,1584977829],[21,1584977832],[21,1584977834],[21,1585052757],[18,1585052760],[23,1585052763],[18,1585052767],[23,1585052769],[24,1585052772],[23,1585052775],[21,1585052777],[23,1585052780],[23,1585052783],[22,1585052785],[22,1585052788],[19,1585052790],[21,1585052793],[23,1585052796],[19,1585052798],[23,1585052801],[21,1585052803],[21,1585052806],[21,1585052808],[21,1585052811],[21,1585052813],[21,1585052816],[21,1585052819],[21,1585052821],[21,1585052824],[21,1585052827],[21,1585052829],[21,1585052832],[21,1585052834],[21,1585052837],[21,1585052839],[21,1585052842],[21,1585052844],[21,1585052847],[21,1585052849],[21,1585052852],[21,1585052854],[21,1585052857],[21,1585052860],[21,1585052862],[21,1585052865],[21,1585052867],[21,1585052870],[21,1585052872],[21,1585052875],[21,1585052877],[21,1585052880],[21,1585052883],[21,1585052885],[21,1585052888],[21,1585053504],[21,1585053507],[21,1585053510],[21,1585053512],[21,1585053515],[21,1585053517],[21,1585053520],[21,1585053523],[21,1585053525],[21,1585053528],[21,1585053530],[21,1585053533],[21,1585053535],[21,1585053538],[21,1585053540],[21,1585053543],[21,1585053545],[21,1585053548],[21,1585053551],[21,1585053553],[21,1585053556],[21,1585053558],[21,1585053561],[21,1585053563],[21,1585053566],[21,1585053569],[21,1585053571],[21,1585053575],[21,1585053578],[21,1585053580],[21,1585053582],[21,1585053590],[21,1585053593],[21,1585053595],[21,1585053598],[21,1585053600],[21,1585053603],[21,1585053605],[21,1585053608],[21,1585053615],[21,1585053618],[21,1585053621],[21,1585053623],[21,1585053626],[21,1585053628],[21,1585053631],[21,1585053633],[21,1585053636],[21,1585053639],[21,1585053641],[21,1585054523],[21,1585054531],[21,1585228804],[21,1585228807],[21,1585229292],[21,1585229294],[21,1585229297],[21,1585229300],[21,1585229302],[21,1585229305],[21,1585229308],[21,1585229310],[21,1585229313],[21,1585229315],[21,1585229318],[21,1585229320],[21,1585229323],[21,1585229326],[21,1585229328],[21,1585229331],[21,1585229333],[21,1585229336],[21,1585229338],[21,1585229341],[21,1585229343],[21,1585229346],[21,1585229349],[21,1585229351],[21,1585229354],[21,1585229356],[21,1585229359],[21,1585229362],[21,1585229364],[21,1585229367],[21,1585229369],[21,1585229372],[21,1585229374],[21,1585229377],[21,1585229379],[21,1585229382],[21,1585229384],[21,1585229387],[21,1585229390],[21,1585229392],[21,1585229395],[21,1585229397],[21,1585229400],[21,1585229403],[21,1585229405],[21,1585229408],[21,1585229410],[21,1585229413],[21,1585229416],[21,1585229418],[21,1585229421],[21,1585229424],[21,1585229426],[21,1585229429],[21,1585229431],[21,1585229434],[21,1585229436],[21,1585229439],[21,1585229441],[21,1585229444],[21,1585229446],[21,1585229449],[21,1585229452],[21,1585229454],[21,1585229457],[21,1585229459],[21,1585229462],[21,1585229464],[21,1585229467],[21,1585229469],[21,1585229472],[21,1585229475],[21,1585229477],[21,1585229480],[21,1585229483],[21,1585229485],[21,1585229488],[21,1585229490],[21,1585229492],[21,1585229495],[21,1585229498],[21,1585229500],[21,1585229503],[21,1585229505],[21,1585229508],[21,1585229510],[21,1585229513],[21,1585229515],[21,1585229518],[21,1585229520],[21,1585229523],[21,1585229527],[21,1585229529],[21,1585229537],[21,1585229539],[21,1585229542],[21,1585229545]]})
print(r.text)