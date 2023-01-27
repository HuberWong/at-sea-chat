//
//  AppDelegate.m
//  ASeaChat-frontend-iOS-OC
//
//  Created by huber wang on 2023/1/22.
//

#import "AppDelegate.h"

@interface AppDelegate ()

@end

@implementation AppDelegate


- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // Override point for customization after application launch.
    
//    ViewController *viewController = [[ViewController alloc] init];
//    self.window.rootViewController = viewController;
//
//    UIView *rootView = [[UIView alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
//    viewController.view = rootView;
//
//    UIButton *button = [UIButton buttonWithType:UIButtonTypeSystem];
//    button.frame = CGRectMake(
//                              (self.window.frame.size.width - 20) / 2,
//                              (self.window.frame.size.height -20) / 2,
//                              20,
//                              20);
//
//    [button setTitle:@"确定" forState:UIControlStateNormal];
//    [rootView addSubview:button];
//
//    self.show = [[UILabel alloc] initWithFrame:CGRectMake(60, 40, 180, 30)];
//    [rootView addSubview:self.show];
//    self.show.text = @"初始文本";
//    self.show.backgroundColor = [UIColor grayColor];
//
//    [button addTarget:self action:@selector(tappedHandler:) forControlEvents:UIControlEventTouchUpInside];
//    [self.window makeKeyAndVisible];
    
    
    

//    NSLog(@"sceneDidBecomeActive");
    
    return YES;
}


#pragma mark - UISceneSession lifecycle


- (UISceneConfiguration *)application:(UIApplication *)application configurationForConnectingSceneSession:(UISceneSession *)connectingSceneSession options:(UISceneConnectionOptions *)options {
    // Called when a new scene session is being created.
    // Use this method to select a configuration to create the new scene with.
    return [[UISceneConfiguration alloc] initWithName:@"Default Configuration" sessionRole:connectingSceneSession.role];
}


- (void)application:(UIApplication *)application didDiscardSceneSessions:(NSSet<UISceneSession *> *)sceneSessions {
    // Called when the user discards a scene session.
    // If any sessions were discarded while the application was not running, this will be called shortly after application:didFinishLaunchingWithOptions.
    // Use this method to release any resources that were specific to the discarded scenes, as they will not return.
}


@end
