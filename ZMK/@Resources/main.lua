function Initialize()
    batteryFile = SELF:GetOption('BatteryFile')
    filePath = SKIN:MakePathAbsolute(batteryFile)
end

function Update()
    local file = io.open(filePath, "r")
    if not file then return "No Data" end

    local batteryLevel = file:read("*all")
    file:close()
    if batteryFile == "C:\\Users\\Luerl\\Documents\\Rainmeter\\Skins\\ZMK\\@Resources\\device_name.txt" then
        return batteryLevel
    else
        return batteryLevel / 100
    end
    
end
