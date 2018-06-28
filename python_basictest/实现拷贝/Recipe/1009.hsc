<?xml version="1.0" encoding="gb2312"?>
<ScrInfo ScreenNo="0" ScreenType="" ScreenSize="0">
	<Script>
		<TimerAction/>
		<TrigAction>
			<Trigger Action="1" BitAddr="HSX4077.0">'设置期数加1
@W_HSW4077 =0 
if @W_HSW4079&lt;@W_HSW4088 then   '当前设置的期数小于总期数
   @W_HSW4079=@W_HSW4079+1
   @W_HSW4073=1'用于触发当前期数信息给start Unit
endif
</Trigger>
			<Trigger Action="1" BitAddr="HSX4078.0">'设置期数减1
@W_HSW4078 =0 
if @W_HSW4079&gt;1 then   '当前设置的期数&gt;0
   @W_HSW4079=@W_HSW4079-1
   @W_HSW4073=1 '用于触发当前期数信息给start Unit
endif



</Trigger>
		</TrigAction>
		<InitialAction>@W_HSW4079=1
@W_HSW4073=1

</InitialAction>
	</Script>
	<PartInfo PartType="WordSwitch" PartName="WS_6">
		<General Desc="WS_1" WordAddr="HSW4075" WriteAddr="HSW4075" DataFormat="2" Const="1" Limit="12" BorderColor="0xcccccc 16777215" BmpIndex="-1" LaStartPt="65 18" Area="0 220 131 257"/>
		<Extension AckTime="20" TouchState="1" Buzzer="1"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" LaIndexID="" CharSize="8 168 168 16"/></PartInfo>
	<PartInfo PartType="WordSwitch" PartName="WS_5">
		<General Desc="WS_1" WordAddr="HSW4075" WriteAddr="HSW4075" DataFormat="2" Const="1" Limit="12" BorderColor="0xcccccc 16777215" BmpIndex="-1" LaStartPt="34 16" Area="138 221 247 257"/>
		<Extension AckTime="20" TouchState="1" Buzzer="1"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" LaIndexID="" CharSize="8 168 168 16"/></PartInfo>
	<PartInfo PartType="Text" PartName="TXT_4">
		<General TextContent="总结算期数：总结算期数：总结算期数：" CharSize="8 168 168 16" StartPt="34 20"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Numeric" PartName="NUM_1">
		<General Desc="NUM_0" WordAddr="HSW4088" IsInput="1" WriteAddr="HSW4088" KbdScreen="-6" BorderColor="0xcccccc 16777215" BgColor="0xffffff 0" BmpIndex="-1" Area="148 12 234 43"/>
		<DispFormat DispType="2" DigitCount="4 0" DataLimit="0 1094713344" Mutiple="1.000000" CharSize="8 16"/>
		<Extension AckTime="20"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Text" PartName="TXT_6">
		<General TextContent="分期密码：分期密码：分期密码：" CharSize="8 168 168 16" StartPt="50 136"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="String" PartName="STR_1">
		<General Desc="STR_0" WordAddr="HSW4090" stCount="8" IsInput="1" WriteAddr="HSW4090" KbdScreen="-1" BorderColor="0xcccccc 16777215" BgColor="0xffffff 0" CharSize="8 16" Area="155 129 351 160"/>
		<Extension AckTime="5"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Text" PartName="TXT_7">
		<General TextContent="目前设置处于:目前设置处于:目前设置处于:" CharSize="8 168 168 16" StartPt="34 89"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Text" PartName="TXT_8">
		<General TextContent="期设置期设置期设置" CharSize="8 168 168 16" StartPt="236 88"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Numeric" PartName="NUM_2">
		<General Desc="NUM_0" WordAddr="HSW4094" IsInput="1" WriteAddr="HSW4094" KbdScreen="-6" BorderColor="0xcccccc 16777215" FrnColor="0xffffff -1" BgColor="0xff8000 -1" BmpIndex="-1" Area="125 175 208 202"/>
		<DispFormat DispType="2" DigitCount="4 0" DataLimit="1156988928 1161527296" Mutiple="1.000000" CharSize="8 16"/>
		<Extension AckTime="20"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Numeric" PartName="NUM_3">
		<General Desc="NUM_0" WordAddr="HSW4095" IsInput="1" WriteAddr="HSW4095" KbdScreen="-6" BorderColor="0xcccccc 16777215" FrnColor="0xffffff -1" BgColor="0xff8000 -1" BmpIndex="-1" Area="249 175 294 202"/>
		<DispFormat DispType="2" DigitCount="2 0" DataLimit="1065353216 1094713344" Mutiple="1.000000" CharSize="8 16"/>
		<Extension AckTime="20"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Numeric" PartName="NUM_4">
		<General Desc="NUM_0" WordAddr="HSW4096" IsInput="1" WriteAddr="HSW4096" KbdScreen="-6" BorderColor="0xcccccc 16777215" FrnColor="0xffffff -1" BgColor="0xff8000 -1" BmpIndex="-1" Area="338 175 387 202"/>
		<DispFormat DispType="2" DigitCount="2 0" DataLimit="1065353216 1106771968" Mutiple="1.000000" CharSize="8 16"/>
		<Extension AckTime="20"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="WordSwitch" PartName="WS_0">
		<General Desc="WS_0" WordAddr="HSW4078" WriteAddr="HSW4078" DataFormat="2" Const="1" FigureFile="真彩型样式\真彩010.pvg" BorderColor="0xffffff 16777215" BmpIndex="-1" Area="2 221 131 257"/>
		<Extension AckTime="20" TouchState="1" Buzzer="1"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" Pattern="-894245163" FrnColor="0xffffff 0" BgColor="0xffffff 0" LaIndexID="上一期上一期上一期" CharSize="8 168 168 16"/></PartInfo>
	<PartInfo PartType="WordSwitch" PartName="WS_1">
		<General Desc="WS_1" WordAddr="HSW4077" WriteAddr="HSW4077" DataFormat="2" Const="1" Limit="12" FigureFile="真彩型样式\真彩010.pvg" BorderColor="0xffffff 16777215" BmpIndex="-1" LaStartPt="34 16" Area="137 221 247 257"/>
		<Extension AckTime="20" TouchState="1" Buzzer="1"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" LaIndexID="下一期下一期下一期" CharSize="8 168 168 16"/></PartInfo>
	<PartInfo PartType="Text" PartName="TXT_0">
		<General TextContent="年年年" CharSize="8 168 168 16" StartPt="226 181"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Text" PartName="TXT_1">
		<General TextContent="月月月" CharSize="8 168 168 16" StartPt="312 181"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Text" PartName="TXT_2">
		<General TextContent="日日日" CharSize="8 168 168 16" StartPt="402 181"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Rect" PartName="REC_1">
		<General LineType="10" BorderColor="0x0 -1" Pattern="-1" FrnColor="0xffffff 0" BgColor="0xffffff 0" Area="35 117 442 213"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Text" PartName="TXT_3">
		<General TextContent="分期时间：分期时间：分期时间：" CharSize="8 168 168 16" StartPt="51 181"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Text" PartName="TXT_9">
		<General TextContent="超级密码：超级密码：超级密码：" CharSize="8 168 168 16" StartPt="35 56"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="String" PartName="STR_0">
		<General Desc="STR_0" WordAddr="HSW4084" stCount="8" IsInput="1" WriteAddr="HSW4084" KbdScreen="-1" BorderColor="0xcccccc 16777215" BgColor="0xffffff 0" CharSize="8 16" Area="140 50 308 81"/>
		<Extension AckTime="5"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Text" PartName="TXT_5">
		<General TextContent="第第第" CharSize="8 168 168 16" StartPt="143 88"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Numeric" PartName="NUM_0">
		<General Desc="NUM_0" WordAddr="HSW4079" KbdScreen="-6" BorderColor="0xcccccc 16777215" FrnColor="0xffffff -1" BgColor="0xff8000 -1" BmpIndex="-1" Area="179 86 220 108"/>
		<DispFormat DispType="2" DigitCount="2 0" DataLimit="0 1120272384" Mutiple="1.000000" CharSize="8 16"/>
		<Extension AckTime="20"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="WordSwitch" PartName="WS_2">
		<General Desc="WS_1" WordAddr="HSW4075" WriteAddr="HSW4075" DataFormat="2" Const="1" Limit="12" FigureFile="真彩型样式\真彩010.pvg" BorderColor="0xffffff 16777215" BmpIndex="-1" LaStartPt="34 16" Area="248 224 318 260"/>
		<Extension AckTime="20" TouchState="1" Buzzer="1"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" LaIndexID="保 存保 存保 存" CharSize="8 168 168 16"/></PartInfo>
	<PartInfo PartType="WordSwitch" PartName="WS_3">
		<General Desc="WS_1" WordAddr="HSW4076" WriteAddr="HSW4076" DataFormat="2" Const="1" Limit="12" FigureFile="真彩型样式\真彩010.pvg" BorderColor="0xffffff 16777215" BmpIndex="-1" LaStartPt="34 16" Area="325 224 395 260"/>
		<Extension AckTime="20" TouchState="1" Buzzer="1"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" LaIndexID="取 消取 消取 消" CharSize="8 168 168 16"/></PartInfo>
	<PartInfo PartType="WordSwitch" PartName="WS_4">
		<General Desc="WS_1" WordAddr="HSW4074" WriteAddr="HSW4074" DataFormat="2" Const="1" Limit="12" FigureFile="真彩型样式\真彩010.pvg" BorderColor="0xffffff 16777215" BmpIndex="-1" LaStartPt="34 16" Area="402 224 472 260"/>
		<Extension AckTime="20" TouchState="1" Buzzer="1"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" Pattern="1" FrnColor="0xffffff 0" BgColor="0xffffff 0" LaIndexID="退 出退 出退 出" CharSize="8 168 168 16"/></PartInfo>
	<PartInfo PartType="Text" PartName="TXT_10">
		<General TextContent="起始期数设置：起始期数设置：起始期数设置：" CharSize="8 168 168 16" StartPt="277 19"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Numeric" PartName="NUM_5">
		<General Desc="NUM_0" WordAddr="HSW4089" IsInput="1" WriteAddr="HSW4089" KbdScreen="-6" BorderColor="0xcccccc 16777215" BgColor="0xffffff 0" BmpIndex="-1" Area="394 12 473 43"/>
		<DispFormat DispType="2" DigitCount="4 0" DataLimit="0 1094713344" Mutiple="1.000000" CharSize="8 16"/>
		<Extension AckTime="20"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo></ScrInfo>
