import discord, globals, asyncio

async def genericmsg(channel,content,status,command):
	embed = discord.Embed(colour=discord.Colour(0x2C5ECA),url=globals.apiurl+"#/"+command,title=(globals.prefix_long+' ' if globals.prefix_long else globals.prefix_short)+command,description=content)

	embed.set_thumbnail(url=globals.emurl+"result.gif")
	embed.set_footer(text=globals.name+" v"+globals.ver+" - created by Yiays#5930", icon_url=globals.iconurl)

	try:
		msg = await channel.send(embed=embed)
	except Exception as e:
		print(e)
		msg = await channel.send(content)
	
	return msg
async def make_embed(channel, message, title, description='', color=0x0063B1, author='', image='', thumbnail='', fields={}, footer='', icon='', link='', **kwargs):
	em=discord.Embed(title=title, type='rich', description=description, color=color, url=link)
	
	if author is not None:
		if author!='': em.set_author(name=author,icon_url=icon)
	
	if thumbnail!='': em.set_thumbnail(url=thumbnail)
	
	if image!='': em.set_image(url=image)
	
	for field in fields:
		em.add_field(name=field+' ', value=fields[field]+' ', inline=True if len(fields[field])<8 else False)
	
	if footer!='': em.set_footer(text=footer,icon_url=icon)
	else: em.set_footer(text=globals.name+" v"+globals.ver+" - created by Yiays#5930")
	
	try:
		if 'edit' not in kwargs:
			msg = await channel.send(message,embed=em)
		else:
			msg = await kwargs['edit'].edit(content=message,embed=em)
	except Exception as e:
		print(e)
		manualfields=''
		for field in fields:
			manualfields+='**'+field+'**\n'+fields[field]+'\n\n'
		if 'edit' not in kwargs:
			msg = await channel.send("{}\n***{}***({})\n{}\n{}{} | ".format(message,title,link,description,manualfields,footer) + f"either {globals.name} is missing `EMBED_LINKS` permission or this embed is too long")
		else:
			msg = await kwargs['edit'].edit(content="{}\n***{}***({})\n{}\n{}{} | ".format(message,title,link,description,manualfields,footer) + f"either {globals.name} is missing `EMBED_LINKS` permission or this embed is too long")
	
	return msg