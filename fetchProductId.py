# url = 'https://www.amazon.in/Sony-MDR-XB450-Ear-EXTRA-Headphones/dp/B00NFKP94O/ref=br_asw_pdt-4?'
# url = 'https://www.amazon.in/gp/product/B00GTJSGXE/ref=s9u_ri_gw_i2?ie='
# url = 'https://www.amazon.in/dp/B01EU2M62S/ref=nav_sh'
# url = 'https://www.amazon.in/GAP-Printed-Regular-18599505001_Shield-Photoreal_Medium/dp/B077MGTB6N/ref=lp_14839'
url = 'https://www.amazon.in/GAP-Printed-Regular-18599505001_Shield-Photoreal_Medium/dp/B077MGTB6N/ref=lp_14839'

if 'www.amazon.in/gp/product/' in url:
	pos = url.find('product/')+8
	product_id = url[pos:pos+10]

else:
	pos = url.find('/dp/')+4
	product_id = url[pos:pos+10]

return product_id