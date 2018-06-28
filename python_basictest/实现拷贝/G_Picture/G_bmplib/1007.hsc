<?xml version="1.0" encoding="gb2312"?>
<ScrInfo ScreenNo="1" ScreenType="" ScreenSize="1">
	<Script>
		<InitialAction>@W_HSW208=0
@W_HSW209=0
</InitialAction>
		<TrigAction>
		</TrigAction>
		<CloseAction></CloseAction></Script>
	<PartInfo PartType="Rect" PartName="REC_0">
		<General BorderColor="0xffffff 0" FrnColor="0xffffff 0" BgColor="0xaa6c6c -1" Area="4 51 227 169"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Rect" PartName="REC_1">
		<General BorderColor="0xffffff 0" FrnColor="0xffffff 0" BgColor="0xaa24fc -1" Area="4 30 227 59"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Text" PartName="TXT_1">
		<General TextContent="本画面用于实时趋势图的基本设置本画面用于实时趋势图的基本设置本画面用于实时趋势图的基本设置" LaFrnColor="0x101010 -1" CharSize="6 126 126 12" StartPt="21 10"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Text" PartName="TXT_0">
		<General TextContent="数据范围设置数据范围设置数据范围设置" LaFrnColor="0xffffff 0" CharSize="6 126 126 12" StartPt="45 31"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Numeric" PartName="NUM_9">
		<General Desc="NUM_0" WordAddr="HSW4587" IsInput="1" WriteAddr="HSW4587" KbdScreen="-6" FigureFile="dpjy_a03.pvg" BorderColor="0xcccccc 0" FrnColor="0xffffff 0" BgColor="0xaa4800 -1" Area="63 124 200 162"/>
		<DispFormat DispType="6" DigitCount="5 0" DataLimit="3338665472 1191181824" Mutiple="1.000000000000" CharSize="6 12"/>
		<Extension/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Numeric" PartName="NUM_10">
		<General Desc="NUM_0" WordAddr="HSW4586" IsInput="1" WriteAddr="HSW4586" KbdScreen="-6" FigureFile="dpjy_a03.pvg" BorderColor="0xcccccc 0" FrnColor="0xffffff 0" BgColor="0xaa4800 -1" Area="63 74 200 108"/>
		<DispFormat DispType="6" DigitCount="5 0" DataLimit="3338665472 1191181824" Mutiple="1.000000000000" CharSize="6 12"/>
		<Extension/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Text" PartName="TXT_12">
		<General TextContent="上限:上限:上限:" LaFrnColor="0xffffff 0" CharSize="6 126 126 12" StartPt="8 79"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Text" PartName="TXT_11">
		<General TextContent="下限:下限:下限:" LaFrnColor="0xffffff 0" CharSize="6 126 126 12" StartPt="8 131"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Text" PartName="TXT_13">
		<General TextContent="

" LaFrnColor="0xffffff 0" CharSize="6 126 126 12" StartPt="12 176"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="WordSwitch" PartName="WS_0">
		<General Desc="WS_0" WordAddr="HSW209" WriteAddr="HSW209" DataFormat="2" Const="1" FigureFile="sw_3d004.pvg" BorderColor="0xcccccc 0" BmpIndex="-1" LaStartPt="15 6" Area="126 262 208 291"/>
		<Extension TouchState="1" Buzzer="1"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" LaIndexID="取 消取 消取 消" CharSize="6 126 126 12" LaFrnColor="0x0 -1"/></PartInfo>
	<PartInfo PartType="WordSwitch" PartName="WS_1">
		<General Desc="WS_0" WordAddr="HSW208" WriteAddr="HSW208" DataFormat="2" Const="1" FigureFile="sw_3d004.pvg" BorderColor="0xcccccc 0" BmpIndex="-1" LaStartPt="107 15" Area="17 262 99 291"/>
		<Extension TouchState="1" Buzzer="1"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" LaIndexID="确 认确 认确 认" CharSize="6 126 126 12" LaFrnColor="0x0 -1"/></PartInfo>
	<PartInfo PartType="Rect" PartName="矩形0">
		<General BorderColor="0xffffff 0" FrnColor="0xffffff 0" BgColor="0xaa6c6c -1" Area="4 170 227 258"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="Text" PartName="文本0">
		<General TextContent="曲线1:曲线1:曲线1:" LaFrnColor="0xffffff 0" CharSize="6 126 126 12" StartPt="10 192"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="BitSwitch" PartName="位开关0">
		<General Desc="BS_0" OperateAddr="HSX8780.0" BitFunc="3" Monitor="1" MonitorAddr="HSX8780.0" FigureFile="swjy_a00.pvg" BorderColor="0xcccccc 0" BmpIndex="-1" Align="3" Area="61 191 116 221"/>
		<Extension TouchState="1" Buzzer="1"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" LaIndexID="禁用禁用禁用" CharSize="6 126 126 12" LaFrnColor="0x0 -1"/>
		<Label Status="1" LaIndexID="启用启用启用" CharSize="12 2424 3224 32" LaFrnColor="0x0 -1"/></PartInfo>
	<PartInfo PartType="Text" PartName="文本1">
		<General TextContent="曲线2:曲线2:曲线2:" LaFrnColor="0xffffff 0" CharSize="6 126 126 12" StartPt="10 227"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="BitSwitch" PartName="位开关1">
		<General Desc="BS_0" OperateAddr="HSX8780.1" BitFunc="3" Monitor="1" MonitorAddr="HSX8780.1" FigureFile="swjy_a00.pvg" BorderColor="0xcccccc 0" BmpIndex="-1" Area="61 221 116 251"/>
		<Extension TouchState="1" Buzzer="1"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" LaIndexID="禁用禁用禁用" CharSize="6 126 126 12" LaFrnColor="0x0 -1"/>
		<Label Status="1" LaIndexID="启用启用启用" CharSize="12 2424 3224 32" LaFrnColor="0x0 -1"/></PartInfo>
	<PartInfo PartType="Text" PartName="文本2">
		<General TextContent="曲线3:曲线3:曲线3:" LaFrnColor="0xffffff 0" CharSize="6 126 126 12" StartPt="122 191"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="BitSwitch" PartName="位开关2">
		<General Desc="BS_0" OperateAddr="HSX8780.2" BitFunc="3" Monitor="1" MonitorAddr="HSX8780.2" FigureFile="swjy_a00.pvg" BorderColor="0xcccccc 0" BmpIndex="-1" Area="171 184 226 214"/>
		<Extension TouchState="1" Buzzer="1"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" LaIndexID="禁用禁用禁用" CharSize="6 126 126 12" LaFrnColor="0x0 -1"/>
		<Label Status="1" LaIndexID="启用启用启用" CharSize="12 2424 3224 32" LaFrnColor="0x0 -1"/></PartInfo>
	<PartInfo PartType="Text" PartName="文本3">
		<General TextContent="曲线4:曲线4:曲线4:" LaFrnColor="0xffffff 0" CharSize="6 126 126 12" StartPt="122 227"/>
		<MoveZoom DataFormatMZ="2"/></PartInfo>
	<PartInfo PartType="BitSwitch" PartName="位开关3">
		<General Desc="BS_0" OperateAddr="HSX8780.3" BitFunc="3" Monitor="1" MonitorAddr="HSX8780.3" FigureFile="swjy_a00.pvg" BorderColor="0xcccccc 0" BmpIndex="-1" Area="171 221 226 251"/>
		<Extension TouchState="1" Buzzer="1"/>
		<MoveZoom DataFormatMZ="2"/>
		<Label Status="0" LaIndexID="禁用禁用禁用" CharSize="6 126 126 12" LaFrnColor="0x0 -1"/>
		<Label Status="1" LaIndexID="启用启用启用" CharSize="12 2424 3224 32" LaFrnColor="0x0 -1"/></PartInfo></ScrInfo>
