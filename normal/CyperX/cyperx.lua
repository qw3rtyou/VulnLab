local base64 = require "base64"
local cyperx = Proto("CyperX", "CyperX Protocol")
local f = cyperx.fields
f.encryption =
    ProtoField.uint16(
    "cyperx.encryption",
    "Encryption",
    base.HEX,
    {
        [0x0312] = "Insecure",
        [0x1105] = "Secure"
    }
)
f.flag = ProtoField.uint8("cyperx.flag", "Flag")
f.size = ProtoField.uint32("cyperx.size", "Size", base.DEC)
f.data = ProtoField.string("cyperx.data", "Data")
f.decoded_data = ProtoField.string("cyperx.decoded_data", "Decoded Data")
function cyperx.dissector(buffer, pinfo, tree)
    pinfo.cols.protocol = "CyperX"
    local subtree = tree:add(cyperx, buffer(), "CyperX Protocol Data")
    local encryption = buffer(0, 4):uint()
    subtree:add(f.encryption, encryption)
    local flag = buffer(4, 2):uint()
    subtree:add(f.flag, flag)
    local size = buffer(6, 4):uint()
    subtree:add(f.size, size)
    if buffer:len() > 8 then
        local data_length = math.min(size, buffer:len() - 8)
        local data_field = buffer(10, data_length)
        subtree:add(f.data, data_field)
        if encryption == 0x0312 then
            decoded_data = data_field:string()
        else
            decoded_data = base64.decode(data_field:string())
        end
        subtree:add(f.decoded_data, decoded_data)
        pinfo.cols.info = string.format("%s", decoded_data)
    end
end
local tcp_port = DissectorTable.get("tcp.port")
tcp_port:add(11111, cyperx)
