import arc
import miru
import hikari
from typing import Any

import src.functions.SpellCodeTranslator as spell

# For more info on plugins & extensions, see: https://arc.hypergonial.com/guides/plugins_extensions/

FILE_LIST = []

plugin = arc.GatewayPlugin("spellcard")
spellcard = plugin.include_slash_group("spellcard", "Generate or translate a .dungeon spellcard.")


def clean_up(ctx: arc.Context[Any]) -> None:
    print(FILE_LIST)
    for x in FILE_LIST:
        print(x)
        spell.delete_file(x)
    FILE_LIST.clear
    print(FILE_LIST)


@spellcard.include
@arc.slash_subcommand("create", "Generate a .dungeon spellcard.")
async def spellcard_command(ctx: arc.GatewayContext, client: miru.Client = arc.inject()) -> None:
    spell_name, spell_desc, spell_cost, spell_skill = create_card_modal()
    modal = Card()
    modal.add_item(spell_name)
    modal.add_item(spell_desc)
    modal.add_item(spell_cost)
    modal.add_item(spell_skill)

    builder = modal.build_response(client)
    await ctx.respond_with_builder(builder)
    client.start_modal(modal)


@spellcard.include
@arc.with_post_hook(clean_up)
@arc.slash_subcommand("read", "Translate a .dungeon spellcard.")
async def spellcard_read(
    ctx: arc.GatewayContext,
    file: arc.Option[hikari.Attachment, arc.AttachmentParams(description="Generated spellcard.", name=None)],
) -> None:
    spellcard = spell.save_file(file.url, "spellcard.png")
    FILE_LIST.append("spellcard.png")
    response = spell.card_read_text(spellcard)
    string = response.split("|")

    await ctx.respond(f"### {string[0]}\n{string[1]}\nCost: {string[2]} // Skill: {string[3]}")


@arc.loader
def load(client: arc.GatewayClient) -> None:
    client.add_plugin(plugin)


@arc.unloader
def unload(client: arc.GatewayClient) -> None:
    client.remove_plugin(plugin)


def create_card_modal():
    spell_name = miru.TextInput(label="Spell Name", custom_id="spellname", max_length=32, required=True)
    spell_desc = miru.TextInput(
        label="Spell Description",
        custom_id="spelldesc",
        max_length=128,
        style=hikari.TextInputStyle.PARAGRAPH,
        required=True,
    )
    spell_cost = miru.TextInput(label="Spell Cost", custom_id="spellcost", max_length=3, required=True)
    spell_skill = miru.TextInput(
        label="Spell Skill", placeholder="Magic, Dreams, or Misc", custom_id="spellskill", required=True
    )
    return spell_name, spell_desc, spell_cost, spell_skill


class Card(miru.Modal, title="Generate a spellcard."):
    # The callback function is called after the user hits 'Submit'
    async def callback(self, ctx: miru.ModalContext) -> None:
        # You can also access the values using ctx.values,
        # Modal.values, or use ctx.get_value_by_id()
        name = ctx.get_value_by_id("spellname")
        desc = ctx.get_value_by_id("spelldesc")
        cost = ctx.get_value_by_id("spellcost")
        skill = ctx.get_value_by_id("spellskill")

        if cost.isdigit():
            pass
        else:
            await ctx.respond("Cost was not a number!", flags=hikari.MessageFlag.EPHEMERAL)
        if skill.capitalize() == "Dreams" or skill.capitalize() == "Magic" or skill.capitalize() == "Misc":
            pass
        else:
            await ctx.respond("Skill was not one of Dreams, Magic, or Misc!", flags=hikari.MessageFlag.EPHEMERAL)

        command_string = f"{name}|{desc}|{cost}|{skill}"
        filename = spell.card_create_spell(command_string)
        print(filename)

        # filename = f"src/functions/{filename.lower()}x10.png"
        # FILE_LIST.append(f"src/functions/{name.lower()}.png")

        await ctx.respond("Your spell has been encoded.")  # , attachment=filename)
