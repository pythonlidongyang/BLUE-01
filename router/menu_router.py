from fastapi import APIRouter

menu_r = APIRouter(tags=["menu"], prefix="/menu")
"""
prefix: str = "",  # 表示当前路由分组的url前缀
tags: Optional[List[Union[str, Enum]]] = None, # 表示当前路由分组在可交互文档中所属的分组标签列表。一个api端点路由可以属于多个分组
dependencies: Optional[Sequence[params.Depends]] = None, # 表示当前路由分组下的依赖项列表。需要注意，这里依赖项列表的返回值不会传递到视图函数内部，也就是说，依赖项的返回值是不会被接收处理的。
default_response_class: Type[Response] = Default(JSONResponse), # 表示设置默认响应报文类，默认返回的JSONResponse
responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None, # 表示根据响应体设置不同的响应报文model模型
callbacks: Optional[List[BaseRoute]] = None, # 回调函数
routes: Optional[List[routing.BaseRoute]] = None, # 路由组
redirect_slashes: bool = True, # 表示是否对路由分组中的斜杠处理进行重定向
default: Optional[ASGIApp] = None,
dependency_overrides_provider: Optional[Any] = None, # 表示当前的依赖注入提供者，默认指向当前的app对象
route_class: Type[APIRoute] = APIRoute, # 表示当前 自定义的APIRoute类
on_startup: Optional[Sequence[Callable[[], Any]]] = None, # 对应app中所提供的启动和关闭事件回调函数
on_shutdown: Optional[Sequence[Callable[[], Any]]] = None,
deprecated: Optional[bool] = None, # 表示是否标记API废弃
include_in_schema: bool = True, # 表示当前路由分组是否显示在可视化交互文档api中
"""


@menu_r.get("/")
async def menu():
    return {
        "code": 200,
        "msg": "hello menu"
    }
