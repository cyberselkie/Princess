import arc

import src.functions.fortune as tarot

# For more info on plugins & extensions, see: https://arc.hypergonial.com/guides/plugins_extensions/

plugin = arc.GatewayPlugin("fortune")


@plugin.include
@arc.slash_command("fortune", "Tell your fortune.")
async def fortune_command(ctx: arc.GatewayContext, query: arc.Option[str, arc.StrParams("Your query.")] = "") -> None:
    fort = tarot.fortunetelling
    if query != "":
        response = f"You're not sure what you want to know, hm? Let us let our dreams guide us...\n{fort}"
    else:
        response = fort
    await ctx.respond(response)


@arc.loader
def load(client: arc.GatewayClient) -> None:
    client.add_plugin(plugin)


@arc.unloader
def unload(client: arc.GatewayClient) -> None:
    client.remove_plugin(plugin)
